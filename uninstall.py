#!/usr/bin/env python3
"""
Spec Agent Uninstaller for Claude Code CLI
汎用仕様書作成Agent群のアンインストーラー
"""

import os
import sys
import shutil
import platform
import json
from pathlib import Path
import argparse

class SpecAgentUninstaller:
    def __init__(self):
        self.system = platform.system()
        self.home = Path.home()
        
        # Claude Code設定ディレクトリ
        if self.system == "Windows":
            self.claude_base = self.home / "AppData" / "Roaming" / "claude-code"
        elif self.system == "Darwin":  # macOS
            self.claude_base = self.home / "Library" / "Application Support" / "claude-code"
        else:  # Linux
            self.claude_base = self.home / ".config" / "claude-code"
        
        self.found_installations = []

    def find_installations(self):
        """インストール済みのspec-agentを検索"""
        locations = []
        
        # ユーザーレベル
        user_path = self.home / ".claude" / "agents" / "spec-agent"
        if user_path.exists():
            locations.append(("user", user_path))
        
        # プロジェクトレベル（現在のディレクトリ）
        project_path = Path.cwd() / ".claude" / "agents"
        if project_path.exists():
            spec_config = project_path / "spec-agent-config.json"
            if spec_config.exists():
                locations.append(("project", project_path))
        
        # Claude Code設定から検索
        claude_config = self.claude_base / "config.json"
        if claude_config.exists():
            try:
                with open(claude_config, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    if "agents" in config and "spec-agent" in config["agents"]:
                        path = Path(config["agents"]["spec-agent"]["path"])
                        if path.exists() and ("config", path) not in locations:
                            locations.append(("config", path))
            except:
                pass
        
        self.found_installations = locations
        return locations

    def display_installations(self):
        """見つかったインストールを表示"""
        if not self.found_installations:
            print("❌ spec-agentのインストールが見つかりません。")
            return False
        
        print("\n以下のインストールが見つかりました:")
        for i, (install_type, path) in enumerate(self.found_installations, 1):
            type_label = {
                "user": "ユーザーレベル",
                "project": "プロジェクトレベル",
                "config": "設定ファイル参照"
            }.get(install_type, install_type)
            
            print(f"{i}. [{type_label}] {path}")
        
        print(f"{len(self.found_installations) + 1}. すべてアンインストール")
        print("0. キャンセル")
        
        return True

    def remove_from_config(self, install_path):
        """設定ファイルからエントリを削除"""
        # ユーザー設定
        claude_config = self.claude_base / "config.json"
        if claude_config.exists():
            try:
                with open(claude_config, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                
                if "agents" in config and "spec-agent" in config["agents"]:
                    if Path(config["agents"]["spec-agent"]["path"]) == install_path:
                        del config["agents"]["spec-agent"]
                        
                        with open(claude_config, 'w', encoding='utf-8') as f:
                            json.dump(config, f, ensure_ascii=False, indent=2)
                        
                        print(f"  ✅ 設定から削除: {claude_config}")
            except Exception as e:
                print(f"  ⚠️  設定の更新に失敗: {e}")
        
        # プロジェクト設定
        project_config = Path.cwd() / ".claude" / "project.json"
        if project_config.exists():
            try:
                with open(project_config, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                
                if "agents" in config and "spec-agent" in config["agents"]:
                    del config["agents"]["spec-agent"]
                    
                    # agentsが空になったら削除
                    if not config["agents"]:
                        del config["agents"]
                    
                    with open(project_config, 'w', encoding='utf-8') as f:
                        json.dump(config, f, ensure_ascii=False, indent=2)
                    
                    print(f"  ✅ プロジェクト設定から削除: {project_config}")
            except Exception as e:
                print(f"  ⚠️  プロジェクト設定の更新に失敗: {e}")

    def uninstall_single(self, install_type, install_path):
        """単一のインストールを削除"""
        print(f"\nアンインストール中: {install_path}")
        
        try:
            # ディレクトリ削除
            if install_path.exists():
                shutil.rmtree(install_path)
                print(f"  ✅ ファイル削除完了")
            
            # 設定から削除
            self.remove_from_config(install_path)
            
            print(f"✅ アンインストール完了: {install_path}")
            return True
            
        except Exception as e:
            print(f"❌ アンインストール失敗: {e}")
            return False

    def uninstall_all(self):
        """すべてのインストールを削除"""
        success_count = 0
        
        for install_type, install_path in self.found_installations:
            if self.uninstall_single(install_type, install_path):
                success_count += 1
        
        return success_count == len(self.found_installations)

    def run(self):
        """アンインストーラーのメイン処理"""
        print("=" * 60)
        print("Spec Agent Uninstaller for Claude Code CLI")
        print("汎用仕様書作成Agent群 アンインストーラー")
        print("=" * 60)
        
        # インストール検索
        self.find_installations()
        
        # 表示
        if not self.display_installations():
            return False
        
        # 選択
        while True:
            try:
                choice = input("\n選択してください: ").strip()
                
                if choice == "0":
                    print("アンインストールをキャンセルしました。")
                    return False
                
                choice_num = int(choice)
                
                if 1 <= choice_num <= len(self.found_installations):
                    # 単一アンインストール
                    install_type, install_path = self.found_installations[choice_num - 1]
                    
                    confirm = input(f"\n本当にアンインストールしますか？ [{install_path}] (y/n): ")
                    if confirm.lower() != 'y':
                        print("キャンセルしました。")
                        return False
                    
                    return self.uninstall_single(install_type, install_path)
                
                elif choice_num == len(self.found_installations) + 1:
                    # 全アンインストール
                    confirm = input("\n本当にすべてアンインストールしますか？ (y/n): ")
                    if confirm.lower() != 'y':
                        print("キャンセルしました。")
                        return False
                    
                    return self.uninstall_all()
                
                else:
                    print("無効な選択です。")
                    
            except ValueError:
                print("数値を入力してください。")
            except KeyboardInterrupt:
                print("\n\nキャンセルしました。")
                return False

def main():
    parser = argparse.ArgumentParser(
        description='Spec Agent uninstaller for Claude Code CLI'
    )
    parser.add_argument('--force', action='store_true',
                       help='Force uninstall without confirmation')
    parser.add_argument('--all', action='store_true',
                       help='Uninstall all installations')
    
    args = parser.parse_args()
    
    uninstaller = SpecAgentUninstaller()
    
    if args.force and args.all:
        # 強制全削除
        uninstaller.find_installations()
        if uninstaller.found_installations:
            result = uninstaller.uninstall_all()
            if result:
                print("\n✅ すべてのspec-agentをアンインストールしました。")
            else:
                print("\n❌ アンインストール中にエラーが発生しました。")
        else:
            print("spec-agentのインストールが見つかりません。")
    else:
        # 対話的アンインストール
        result = uninstaller.run()
        
        if result:
            print("\n" + "=" * 60)
            print("✅ アンインストール完了！")
            print("=" * 60)

if __name__ == "__main__":
    main()