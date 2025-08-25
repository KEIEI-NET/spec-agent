#!/usr/bin/env python3
"""
Spec Agent Installer for Claude Code CLI (改善版)
汎用仕様書作成Agent群のインストーラー
"""

import os
import sys
import shutil
import platform
import json
import tempfile
import logging
from pathlib import Path
import argparse
import subprocess
from datetime import datetime

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SpecAgentInstaller:
    def __init__(self):
        self.system = platform.system()
        self.home = Path.home()
        self.script_dir = Path(__file__).parent.resolve()
        self.backup_dir = None
        
        # Claude Code設定ディレクトリの検出
        if self.system == "Windows":
            self.claude_base = self.home / "AppData" / "Roaming" / "claude-code"
        elif self.system == "Darwin":  # macOS
            self.claude_base = self.home / "Library" / "Application Support" / "claude-code"
        else:  # Linux
            self.claude_base = self.home / ".config" / "claude-code"
        
        # エージェントファイル
        self.agent_files = [
            "spec-master-agent.md",
            "requirement-analyst-agent.md",
            "system-architect-agent.md",
            "implementation-spec-agent.md",
            "technical-writer-agent.md",
            "qa-reviewer-agent.md",
            "coordination_rules.yaml"
        ]
        
        # テンプレートファイル
        self.template_files = [
            "progress.md",
            "todo.md"
        ]

    def check_permissions(self, path):
        """ディレクトリへの書き込み権限を確認"""
        try:
            test_file = path / ".test_write_permission"
            test_file.touch()
            test_file.unlink()
            return True
        except (PermissionError, OSError) as e:
            logger.error(f"書き込み権限がありません: {path}")
            return False

    def check_disk_space(self, path, required_mb=10):
        """必要なディスク容量を確認"""
        try:
            stat = shutil.disk_usage(path)
            free_mb = stat.free / (1024 * 1024)
            if free_mb < required_mb:
                logger.error(f"ディスク容量不足: {free_mb:.1f}MB < {required_mb}MB")
                return False
            return True
        except Exception as e:
            logger.warning(f"ディスク容量の確認に失敗: {e}")
            return True  # 確認できない場合は続行

    def check_claude_code(self):
        """Claude Codeのインストール確認とバージョンチェック"""
        try:
            # コマンドを安全に実行
            if self.system == "Windows":
                result = subprocess.run(
                    ["cmd", "/c", "claude", "--version"],
                    capture_output=True, 
                    text=True,
                    timeout=5
                )
            else:
                result = subprocess.run(
                    ["claude", "--version"],
                    capture_output=True, 
                    text=True,
                    timeout=5
                )
            
            if result.returncode == 0:
                version = result.stdout.strip()
                print(f"✅ Claude Code CLI が検出されました: {version}")
                return True
        except subprocess.TimeoutExpired:
            logger.error("Claude Code CLIの確認がタイムアウトしました")
        except Exception as e:
            logger.error(f"Claude Code CLIの確認中にエラー: {e}")
        
        print("❌ Claude Code CLI が見つかりません")
        print("   以下のコマンドでインストールしてください:")
        print("   npm install -g @anthropic-ai/claude-code")
        return False

    def validate_files(self):
        """必要なファイルの存在確認"""
        missing_files = []
        for file in self.agent_files + self.template_files:
            if not (self.script_dir / file).exists():
                missing_files.append(file)
        
        if missing_files:
            logger.error(f"必要なファイルが見つかりません: {', '.join(missing_files)}")
            return False
        return True

    def select_installation_type(self):
        """インストールタイプの選択"""
        print("\nインストールタイプを選択してください:")
        print("1. ユーザーレベル（このユーザー専用）")
        print("2. プロジェクトレベル（現在のプロジェクトのみ）")
        
        max_attempts = 3
        for _ in range(max_attempts):
            try:
                choice = input("\n選択 (1 or 2): ").strip()
                if choice == "1":
                    return "user"
                elif choice == "2":
                    return "project"
                else:
                    print("無効な選択です。1 または 2 を入力してください。")
            except KeyboardInterrupt:
                print("\n\nインストールをキャンセルしました。")
                sys.exit(0)
        
        logger.error("有効な選択が入力されませんでした")
        return None

    def get_installation_path(self, install_type):
        """インストールパスの取得"""
        if install_type == "user":
            return self.home / ".claude" / "agents" / "spec-agent"
        else:
            return Path.cwd() / ".claude" / "agents"

    def backup_existing(self, install_path):
        """既存インストールのバックアップ"""
        if not install_path.exists():
            return True
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.backup_dir = install_path.parent / f"spec-agent_backup_{timestamp}"
            shutil.copytree(install_path, self.backup_dir)
            logger.info(f"既存インストールをバックアップ: {self.backup_dir}")
            return True
        except Exception as e:
            logger.error(f"バックアップの作成に失敗: {e}")
            return False

    def create_config(self, install_path, install_type):
        """設定ファイルの作成"""
        config = {
            "name": "spec-agent",
            "version": "1.0.1",
            "type": install_type,
            "description": "汎用仕様書作成Agent群",
            "installed_at": datetime.now().isoformat(),
            "agents": {
                "spec-master": {
                    "file": "spec-master-agent.md",
                    "description": "仕様書作成プロセス全体を管理"
                },
                "requirement-analyst": {
                    "file": "requirement-analyst-agent.md",
                    "description": "要求分析専門"
                },
                "system-architect": {
                    "file": "system-architect-agent.md",
                    "description": "システム設計専門"
                },
                "implementation-spec": {
                    "file": "implementation-spec-agent.md",
                    "description": "実装仕様専門"
                },
                "technical-writer": {
                    "file": "technical-writer-agent.md",
                    "description": "ドキュメント整形専門"
                },
                "qa-reviewer": {
                    "file": "qa-reviewer-agent.md",
                    "description": "品質レビュー専門"
                }
            },
            "templates": {
                "progress": "templates/progress.md",
                "todo": "templates/todo.md"
            },
            "rules": "coordination_rules.yaml"
        }
        
        config_file = install_path / "spec-agent-config.json"
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            return config_file
        except Exception as e:
            logger.error(f"設定ファイルの作成に失敗: {e}")
            return None

    def copy_files(self, install_path):
        """ファイルのコピー（エラーハンドリング強化）"""
        copied_files = []
        try:
            # エージェントファイルのコピー
            for file in self.agent_files:
                src = self.script_dir / file
                dst = install_path / file
                if src.exists():
                    shutil.copy2(src, dst)
                    copied_files.append(dst)
                    print(f"  ✅ {file}")
                else:
                    logger.warning(f"  ⚠️  {file} が見つかりません")
            
            # テンプレートファイルのコピー
            templates_dir = install_path / "templates"
            templates_dir.mkdir(exist_ok=True)
            
            for file in self.template_files:
                src = self.script_dir / file
                dst = templates_dir / file
                if src.exists():
                    shutil.copy2(src, dst)
                    copied_files.append(dst)
                    print(f"  ✅ templates/{file}")
            
            return True
        
        except Exception as e:
            logger.error(f"ファイルコピー中にエラー: {e}")
            # ロールバック
            for file in copied_files:
                try:
                    file.unlink()
                except:
                    pass
            return False

    def create_activation_script(self, install_path, install_type):
        """アクティベーションスクリプトの作成（エラーハンドリング強化）"""
        try:
            if install_type == "user":
                claude_config = self.claude_base / "config.json"
                
                # 既存設定のバックアップ
                if claude_config.exists():
                    backup = claude_config.with_suffix('.json.bak')
                    shutil.copy2(claude_config, backup)
                    
                    with open(claude_config, 'r', encoding='utf-8') as f:
                        config = json.load(f)
                else:
                    config = {}
                
                if "agents" not in config:
                    config["agents"] = {}
                
                config["agents"]["spec-agent"] = {
                    "path": str(install_path),
                    "enabled": True
                }
                
                claude_config.parent.mkdir(parents=True, exist_ok=True)
                with open(claude_config, 'w', encoding='utf-8') as f:
                    json.dump(config, f, ensure_ascii=False, indent=2)
                
                print(f"\n✅ ユーザー設定に追加されました: {claude_config}")
            
            else:
                project_config = Path.cwd() / ".claude" / "project.json"
                
                # 既存設定のバックアップ
                if project_config.exists():
                    backup = project_config.with_suffix('.json.bak')
                    shutil.copy2(project_config, backup)
                    
                    with open(project_config, 'r', encoding='utf-8') as f:
                        config = json.load(f)
                else:
                    config = {"name": Path.cwd().name}
                
                config["agents"] = {
                    "spec-agent": {
                        "path": "./agents",
                        "enabled": True
                    }
                }
                
                project_config.parent.mkdir(parents=True, exist_ok=True)
                with open(project_config, 'w', encoding='utf-8') as f:
                    json.dump(config, f, ensure_ascii=False, indent=2)
                
                print(f"\n✅ プロジェクト設定に追加されました: {project_config}")
            
            return True
            
        except Exception as e:
            logger.error(f"アクティベーション設定の作成に失敗: {e}")
            return False

    def rollback(self):
        """インストール失敗時のロールバック"""
        if self.backup_dir and self.backup_dir.exists():
            try:
                original_path = self.backup_dir.parent / "spec-agent"
                if original_path.exists():
                    shutil.rmtree(original_path)
                shutil.move(str(self.backup_dir), str(original_path))
                logger.info("ロールバックが完了しました")
            except Exception as e:
                logger.error(f"ロールバックに失敗: {e}")

    def install(self):
        """インストール実行"""
        print("=" * 60)
        print("Spec Agent Installer for Claude Code CLI (v1.0.1)")
        print("汎用仕様書作成Agent群 インストーラー")
        print("=" * 60)
        
        # 前提条件チェック
        if not self.check_claude_code():
            return False
        
        if not self.validate_files():
            return False
        
        # インストールタイプ選択
        install_type = self.select_installation_type()
        if not install_type:
            return False
        
        # インストールパス決定
        install_path = self.get_installation_path(install_type)
        
        print(f"\nインストール先: {install_path}")
        
        # 権限チェック
        if not self.check_permissions(install_path.parent):
            print("❌ インストール先への書き込み権限がありません")
            if self.system != "Windows":
                print("   sudoで実行するか、権限を確認してください")
            return False
        
        # ディスク容量チェック
        if not self.check_disk_space(install_path.parent):
            return False
        
        # 既存インストールの確認とバックアップ
        if install_path.exists():
            response = input("\n既にインストールされています。上書きしますか？ (y/n): ")
            if response.lower() != 'y':
                print("インストールをキャンセルしました。")
                return False
            
            if not self.backup_existing(install_path):
                print("バックアップの作成に失敗しました。続行しますか？ (y/n): ")
                if input().lower() != 'y':
                    return False
            
            shutil.rmtree(install_path)
        
        # ディレクトリ作成
        install_path.mkdir(parents=True, exist_ok=True)
        
        print("\nファイルをコピー中...")
        
        # インストール実行
        success = True
        
        # ファイルコピー
        if not self.copy_files(install_path):
            success = False
        
        # 設定ファイル作成
        if success:
            config_file = self.create_config(install_path, install_type)
            if config_file:
                print(f"\n設定ファイル作成: {config_file}")
            else:
                success = False
        
        # アクティベーションスクリプト作成
        if success:
            if not self.create_activation_script(install_path, install_type):
                success = False
        
        # 結果表示
        if success:
            print("\n" + "=" * 60)
            print("✅ インストール完了！")
            print("\n使用方法:")
            print("1. Claude Codeを起動: claude")
            print("2. 以下のコマンドでAgent を呼び出し:")
            print("   @spec-master-agent プロジェクトを開始します")
            print("\n詳細は manual.md を参照してください。")
            print("=" * 60)
        else:
            print("\n❌ インストールに失敗しました")
            self.rollback()
            return False
        
        return True

def main():
    parser = argparse.ArgumentParser(
        description='Spec Agent installer for Claude Code CLI'
    )
    parser.add_argument('--uninstall', action='store_true',
                       help='Uninstall spec agents')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    installer = SpecAgentInstaller()
    
    if args.uninstall:
        print("アンインストール機能は別途 uninstall.py を使用してください。")
    else:
        try:
            success = installer.install()
            sys.exit(0 if success else 1)
        except KeyboardInterrupt:
            print("\n\nインストールがユーザーによって中断されました。")
            installer.rollback()
            sys.exit(1)
        except Exception as e:
            logger.error(f"予期しないエラー: {e}")
            installer.rollback()
            sys.exit(1)

if __name__ == "__main__":
    main()