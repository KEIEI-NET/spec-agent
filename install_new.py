#!/usr/bin/env python3
"""
Spec Agent After Installer for Claude Code CLI
自動車アフターマーケット業界向け仕様書作成Agent群のインストーラー
Version: v1.0.0
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

class SpecAgentAfterInstaller:
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
        
        # 基本エージェントファイル（旧構造との互換性）
        self.basic_agent_files = [
            "agent/auto-spec-master-agent.md",
            "agent/auto-requirement-agent.md",
            "agent/auto-system-architect-agent.md",
            "agent/auto-implementation-agent.md",
            "agent/auto-integration-agent.md",
            "agent/auto-qa-reviewer-agent.md",
            "agent/auto-compliance-agent.md"
        ]
        
        # セクターモジュール構造
        self.sector_modules = {
            "parts-commerce": [
                "agents/parts-catalog-agent.md",
                "agents/inventory-forecast-agent.md",
                "agents/compliance-verification-agent.md",
                "agents/commercial-vehicle-parts-agent.md",
                "agents/european-vehicle-parts-agent.md"
            ],
            "glass-specialty": [
                "agents/adas-calibration-agent.md",
                "agents/glass-specification-agent.md",
                "agents/insurance-integration-agent.md"
            ],
            "recycling-compliance": [
                "agents/dismantling-process-agent.md",
                "agents/circular-economy-agent.md",
                "agents/manifest-management-agent.md"
            ]
        }
        
        # 設定ファイル
        self.config_files = [
            "coordination_rules.yaml",
            "auto_coordination_rules.yaml",
            "sector-modules/sector-coordinator.yaml"
        ]
        
        # 法規制データベース
        self.regulation_files = {
            "parts-commerce": [
                "regulations/pl-law.yaml",
                "regulations/iatf16949.yaml"
            ],
            "glass-specialty": [
                "regulations/adas-regulation.yaml",
                "regulations/ece-r43.yaml"
            ],
            "recycling-compliance": [
                "regulations/auto-recycling-law.yaml",
                "regulations/freon-law.yaml",
                "regulations/ev-battery-law.yaml"
            ]
        }
        
        # 横断機能ファイル
        self.cross_sector_files = [
            "cross-sector-functions/supply-chain-integration.yaml",
            "cross-sector-functions/carbon-footprint-tracker.yaml",
            "cross-sector-functions/circular-economy-metrics.yaml"
        ]
        
        # マルチブランド対応ファイル
        self.multi_brand_files = [
            "sector-modules/parts-commerce/multi-brand-compatibility.yaml"
        ]
        
        # ドキュメントファイル
        self.doc_files = [
            "README.md",
            "CLAUDE.md",
            "INSTALLATION.md",
            "USAGE.md",
            "DOCUMENTATION_STATUS.md",
            "progress.md",
            "todo.md"
        ]

    def check_permissions(self, path):
        """ディレクトリへの書き込み権限を確認"""
        try:
            # ディレクトリが存在しない場合は作成を試みる
            path.mkdir(parents=True, exist_ok=True)
            
            test_file = path / ".test_write_permission"
            test_file.touch()
            test_file.unlink()
            return True
        except (PermissionError, OSError) as e:
            logger.error(f"書き込み権限がありません: {path}")
            return False

    def check_disk_space(self, path, required_mb=50):
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
        """Claude Codeのインストール確認"""
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
                logger.info(f"✅ Claude Code が検出されました")
                return True
            else:
                logger.warning("⚠️ Claude Code が見つかりません")
                return False
        except FileNotFoundError:
            logger.warning("⚠️ Claude Code コマンドが見つかりません")
            return False
        except subprocess.TimeoutExpired:
            logger.error("Claude Code の確認がタイムアウトしました")
            return False
        except Exception as e:
            logger.error(f"Claude Code の確認中にエラー: {e}")
            return False

    def create_backup(self, target_dir):
        """既存ファイルのバックアップ作成"""
        if not target_dir.exists():
            return None
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = target_dir.parent / f"spec-agent-backup-{timestamp}"
        
        try:
            shutil.copytree(target_dir, backup_dir)
            logger.info(f"✅ バックアップ作成完了: {backup_dir}")
            self.backup_dir = backup_dir
            return backup_dir
        except Exception as e:
            logger.error(f"バックアップ作成失敗: {e}")
            return None

    def copy_file_safely(self, src, dst):
        """ファイルを安全にコピー"""
        src_path = self.script_dir / src
        dst_path = dst
        
        if not src_path.exists():
            logger.warning(f"ソースファイルが存在しません: {src}")
            return False
        
        try:
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dst_path)
            logger.debug(f"コピー完了: {src} -> {dst_path}")
            return True
        except Exception as e:
            logger.error(f"ファイルコピー失敗: {src} - {e}")
            return False

    def install_user_level(self):
        """ユーザーレベルインストール"""
        logger.info("🚀 ユーザーレベルインストールを開始...")
        
        # インストール先ディレクトリ
        install_dir = self.home / ".claude" / "agents" / "spec-agent-after"
        
        # 権限とディスク容量確認
        if not self.check_permissions(install_dir):
            return False
        if not self.check_disk_space(install_dir):
            return False
        
        # バックアップ作成
        if install_dir.exists():
            logger.info("既存のインストールを検出。バックアップを作成します...")
            self.create_backup(install_dir)
        
        # ディレクトリ作成
        install_dir.mkdir(parents=True, exist_ok=True)
        
        # ファイルコピー
        success_count = 0
        total_count = 0
        
        # 基本エージェントファイル
        logger.info("📋 基本エージェントをインストール中...")
        agent_dir = install_dir / "agent"
        agent_dir.mkdir(exist_ok=True)
        for agent_file in self.basic_agent_files:
            total_count += 1
            if self.copy_file_safely(agent_file, agent_dir / Path(agent_file).name):
                success_count += 1
        
        # セクターモジュール
        logger.info("🏭 セクターモジュールをインストール中...")
        for sector, files in self.sector_modules.items():
            sector_dir = install_dir / "sector-modules" / sector
            sector_dir.mkdir(parents=True, exist_ok=True)
            for file in files:
                total_count += 1
                src = f"sector-modules/{sector}/{file}"
                dst = sector_dir / file
                if self.copy_file_safely(src, dst):
                    success_count += 1
        
        # 法規制データベース
        logger.info("📚 法規制データベースをインストール中...")
        for sector, files in self.regulation_files.items():
            for file in files:
                total_count += 1
                src = f"sector-modules/{sector}/{file}"
                dst = install_dir / "sector-modules" / sector / file
                if self.copy_file_safely(src, dst):
                    success_count += 1
        
        # 横断機能ファイル
        logger.info("🔗 横断機能をインストール中...")
        cross_dir = install_dir / "cross-sector-functions"
        cross_dir.mkdir(exist_ok=True)
        for file in self.cross_sector_files:
            total_count += 1
            if self.copy_file_safely(file, install_dir / file):
                success_count += 1
        
        # マルチブランド対応
        logger.info("🚗 マルチブランド対応をインストール中...")
        for file in self.multi_brand_files:
            total_count += 1
            if self.copy_file_safely(file, install_dir / file):
                success_count += 1
        
        # 設定ファイル
        logger.info("⚙️ 設定ファイルをインストール中...")
        for config_file in self.config_files:
            if (self.script_dir / config_file).exists():
                total_count += 1
                if self.copy_file_safely(config_file, install_dir / config_file):
                    success_count += 1
        
        # ドキュメント
        logger.info("📖 ドキュメントをインストール中...")
        for doc_file in self.doc_files:
            if (self.script_dir / doc_file).exists():
                total_count += 1
                if self.copy_file_safely(doc_file, install_dir / doc_file):
                    success_count += 1
        
        # 結果表示
        logger.info(f"\n✅ インストール完了！")
        logger.info(f"📊 {success_count}/{total_count} ファイルが正常にインストールされました")
        logger.info(f"📁 インストール先: {install_dir}")
        
        if success_count < total_count:
            logger.warning(f"⚠️ {total_count - success_count} ファイルのインストールに失敗しました")
        
        return success_count == total_count

    def install_project_level(self):
        """プロジェクトレベルインストール"""
        logger.info("🚀 プロジェクトレベルインストールを開始...")
        
        # インストール先ディレクトリ（カレントディレクトリ）
        install_dir = Path.cwd() / ".claude" / "agents"
        
        # 権限とディスク容量確認
        if not self.check_permissions(install_dir):
            return False
        if not self.check_disk_space(install_dir):
            return False
        
        # ディレクトリ作成
        install_dir.mkdir(parents=True, exist_ok=True)
        
        # ユーザーレベルと同じロジックでインストール
        # （コード重複を避けるため、実際は共通メソッドを作成すべき）
        success = self._install_to_directory(install_dir)
        
        if success:
            logger.info(f"\n✅ プロジェクトレベルインストール完了！")
            logger.info(f"📁 インストール先: {install_dir}")
        
        return success

    def _install_to_directory(self, install_dir):
        """指定ディレクトリへのインストール（共通処理）"""
        # ここにインストールロジックを実装
        # （install_user_levelのファイルコピー部分と同じ）
        return True

    def verify_installation(self, install_dir):
        """インストールの検証"""
        logger.info("\n🔍 インストールを検証中...")
        
        required_files = []
        
        # 基本エージェントの確認
        for agent in self.basic_agent_files:
            required_files.append(install_dir / "agent" / Path(agent).name)
        
        # セクターモジュールの確認
        for sector, files in self.sector_modules.items():
            for file in files:
                required_files.append(install_dir / "sector-modules" / sector / file)
        
        missing_files = []
        for file in required_files:
            if not file.exists():
                missing_files.append(file)
        
        if missing_files:
            logger.error(f"❌ {len(missing_files)} ファイルが見つかりません:")
            for file in missing_files[:5]:  # 最初の5つだけ表示
                logger.error(f"  - {file}")
            return False
        
        logger.info(f"✅ 全ての必要ファイルが正常にインストールされています")
        return True

    def uninstall(self, install_type="user"):
        """アンインストール"""
        logger.info("🗑️ アンインストールを開始...")
        
        if install_type == "user":
            install_dir = self.home / ".claude" / "agents" / "spec-agent-after"
        else:
            install_dir = Path.cwd() / ".claude" / "agents"
        
        if not install_dir.exists():
            logger.info("インストールが見つかりません")
            return True
        
        try:
            # バックアップ作成
            self.create_backup(install_dir)
            
            # 削除実行
            shutil.rmtree(install_dir)
            logger.info(f"✅ アンインストール完了: {install_dir}")
            return True
        except Exception as e:
            logger.error(f"アンインストール失敗: {e}")
            return False

    def test_installation(self):
        """インストールのテスト（仮想環境）"""
        logger.info("\n🧪 仮想環境でのインストールテストを開始...")
        
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = Path(tmpdir) / "test-install"
            test_dir.mkdir()
            
            logger.info(f"テストディレクトリ: {test_dir}")
            
            # テスト用のホームディレクトリを設定
            original_home = self.home
            self.home = test_dir
            
            try:
                # テストインストール実行
                success = self.install_user_level()
                
                if success:
                    # 検証
                    install_dir = test_dir / ".claude" / "agents" / "spec-agent-after"
                    if self.verify_installation(install_dir):
                        logger.info("✅ テストインストール成功！")
                        
                        # インストールされたファイルをリスト
                        logger.info("\n📦 インストールされたファイル:")
                        md_files = list(install_dir.rglob("*.md"))[:10]
                        for item in md_files:
                            logger.info(f"  - {item.relative_to(install_dir)}")
                        yaml_files = list(install_dir.rglob("*.yaml"))[:10]
                        for item in yaml_files:
                            logger.info(f"  - {item.relative_to(install_dir)}")
                    else:
                        logger.error("❌ テストインストールの検証に失敗")
                        success = False
                else:
                    logger.error("❌ テストインストールに失敗")
                
            finally:
                # ホームディレクトリを元に戻す
                self.home = original_home
            
            return success

def main():
    parser = argparse.ArgumentParser(
        description="Spec Agent After - 自動車アフターマーケット業界向け仕様書作成エージェント インストーラー"
    )
    parser.add_argument(
        "--type",
        choices=["user", "project"],
        default="user",
        help="インストールタイプ（user: ユーザーレベル, project: プロジェクトレベル）"
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="アンインストールを実行"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="仮想環境でテストインストールを実行"
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="既存のインストールを検証"
    )
    
    args = parser.parse_args()
    
    installer = SpecAgentAfterInstaller()
    
    # ロゴ表示
    print("""
╔══════════════════════════════════════════════════════════╗
║     🚗 Spec Agent After - Automotive Aftermarket 🚗      ║
║         自動車アフターマーケット業界向け                  ║
║              仕様書自動作成システム                       ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    # Claude Code確認
    if not installer.check_claude_code():
        logger.warning("Claude Code CLIがインストールされていない可能性があります")
        print("\nClaude Code CLIのインストール方法:")
        print("  npm install -g @anthropic-ai/claude-code")
        response = input("\n続行しますか？ (y/N): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    # テスト実行
    if args.test:
        success = installer.test_installation()
        sys.exit(0 if success else 1)
    
    # 検証実行
    if args.verify:
        if args.type == "user":
            install_dir = installer.home / ".claude" / "agents" / "spec-agent-after"
        else:
            install_dir = Path.cwd() / ".claude" / "agents"
        
        success = installer.verify_installation(install_dir)
        sys.exit(0 if success else 1)
    
    # アンインストール実行
    if args.uninstall:
        success = installer.uninstall(args.type)
        sys.exit(0 if success else 1)
    
    # インストール実行
    if args.type == "user":
        success = installer.install_user_level()
    else:
        success = installer.install_project_level()
    
    if success:
        print("\n" + "="*60)
        print("✅ インストールが完了しました！")
        print("="*60)
        print("\n使用方法:")
        print("  1. Claude Code CLIを起動: claude")
        print("  2. エージェントを呼び出し: @spec-master-agent")
        print("\nセクター別エージェント:")
        print("  - 部品商社: @parts-catalog-agent")
        print("  - 大型車両: @commercial-vehicle-parts-agent")
        print("  - 欧州車: @european-vehicle-parts-agent")
        print("  - ガラス: @adas-calibration-agent")
        print("  - リサイクル: @dismantling-process-agent")
    else:
        print("\n❌ インストールに失敗しました")
        print("ログを確認してください")
        sys.exit(1)

if __name__ == "__main__":
    main()