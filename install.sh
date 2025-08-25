#!/bin/bash

# Spec Agent Installer for Claude Code CLI (Unix/Linux/macOS)
# 汎用仕様書作成Agent群のインストーラー

set -e

# 色付き出力
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# スクリプトのディレクトリ
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# OS検出
OS=$(uname -s)
case "$OS" in
    Darwin*)
        OS_NAME="macOS"
        CLAUDE_BASE="$HOME/Library/Application Support/claude-code"
        ;;
    Linux*)
        OS_NAME="Linux"
        CLAUDE_BASE="$HOME/.config/claude-code"
        ;;
    *)
        echo -e "${RED}サポートされていないOS: $OS${NC}"
        exit 1
        ;;
esac

echo "============================================================"
echo "Spec Agent Installer for Claude Code CLI"
echo "汎用仕様書作成Agent群 インストーラー"
echo "OS: $OS_NAME"
echo "============================================================"

# Claude Code確認
check_claude_code() {
    if command -v claude &> /dev/null; then
        echo -e "${GREEN}✅ Claude Code CLI が検出されました${NC}"
        return 0
    else
        echo -e "${RED}❌ Claude Code CLI が見つかりません${NC}"
        echo "   以下のコマンドでインストールしてください:"
        echo "   npm install -g @anthropic-ai/claude-code"
        return 1
    fi
}

# インストールタイプ選択
select_install_type() {
    echo ""
    echo "インストールタイプを選択してください:"
    echo "1. ユーザーレベル（このユーザー専用）"
    echo "2. プロジェクトレベル（現在のプロジェクトのみ）"
    echo ""
    
    while true; do
        read -p "選択 (1 or 2): " choice
        case $choice in
            1)
                echo "user"
                return
                ;;
            2)
                echo "project"
                return
                ;;
            *)
                echo "無効な選択です。1 または 2 を入力してください。"
                ;;
        esac
    done
}

# インストールパス取得
get_install_path() {
    local install_type=$1
    
    if [ "$install_type" = "user" ]; then
        echo "$HOME/.claude/agents/spec-agent"
    else
        echo "$(pwd)/.claude/agents"
    fi
}

# ファイルコピー
copy_files() {
    local install_path=$1
    
    echo "ファイルをコピー中..."
    
    # エージェントファイル
    for file in spec-master-agent.md requirement-analyst-agent.md \
                system-architect-agent.md implementation-spec-agent.md \
                technical-writer-agent.md qa-reviewer-agent.md \
                coordination_rules.yaml; do
        if [ -f "$SCRIPT_DIR/$file" ]; then
            cp "$SCRIPT_DIR/$file" "$install_path/"
            echo -e "  ${GREEN}✅${NC} $file"
        else
            echo -e "  ${YELLOW}⚠️${NC}  $file が見つかりません"
        fi
    done
    
    # テンプレートファイル
    mkdir -p "$install_path/templates"
    for file in progress.md todo.md; do
        if [ -f "$SCRIPT_DIR/$file" ]; then
            cp "$SCRIPT_DIR/$file" "$install_path/templates/"
            echo -e "  ${GREEN}✅${NC} templates/$file"
        fi
    done
}

# 設定ファイル作成
create_config() {
    local install_path=$1
    local install_type=$2
    
    cat > "$install_path/spec-agent-config.json" << EOF
{
  "name": "spec-agent",
  "version": "1.0.0",
  "type": "$install_type",
  "description": "汎用仕様書作成Agent群",
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
EOF
    
    echo -e "${GREEN}設定ファイル作成: $install_path/spec-agent-config.json${NC}"
}

# アクティベーション設定
activate_agents() {
    local install_path=$1
    local install_type=$2
    
    if [ "$install_type" = "user" ]; then
        # ユーザーレベル設定
        local config_file="$CLAUDE_BASE/config.json"
        mkdir -p "$(dirname "$config_file")"
        
        if [ -f "$config_file" ]; then
            # 既存の設定に追加（jqが必要）
            if command -v jq &> /dev/null; then
                jq --arg path "$install_path" \
                   '.agents["spec-agent"] = {"path": $path, "enabled": true}' \
                   "$config_file" > "$config_file.tmp" && \
                   mv "$config_file.tmp" "$config_file"
            else
                echo -e "${YELLOW}jqがインストールされていないため、手動で設定を追加してください${NC}"
            fi
        else
            # 新規作成
            cat > "$config_file" << EOF
{
  "agents": {
    "spec-agent": {
      "path": "$install_path",
      "enabled": true
    }
  }
}
EOF
        fi
        echo -e "${GREEN}✅ ユーザー設定に追加されました: $config_file${NC}"
        
    else
        # プロジェクトレベル設定
        local project_config="$(pwd)/.claude/project.json"
        mkdir -p "$(dirname "$project_config")"
        
        cat > "$project_config" << EOF
{
  "name": "$(basename "$(pwd)")",
  "agents": {
    "spec-agent": {
      "path": "./agents",
      "enabled": true
    }
  }
}
EOF
        echo -e "${GREEN}✅ プロジェクト設定に追加されました: $project_config${NC}"
    fi
}

# メイン処理
main() {
    # Claude Code確認
    if ! check_claude_code; then
        exit 1
    fi
    
    # インストールタイプ選択
    INSTALL_TYPE=$(select_install_type)
    
    # インストールパス決定
    INSTALL_PATH=$(get_install_path "$INSTALL_TYPE")
    
    echo ""
    echo "インストール先: $INSTALL_PATH"
    
    # 既存インストール確認
    if [ -d "$INSTALL_PATH" ]; then
        read -p "既にインストールされています。上書きしますか？ (y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "インストールをキャンセルしました。"
            exit 0
        fi
        rm -rf "$INSTALL_PATH"
    fi
    
    # ディレクトリ作成
    mkdir -p "$INSTALL_PATH"
    
    # ファイルコピー
    copy_files "$INSTALL_PATH"
    
    # 設定ファイル作成
    create_config "$INSTALL_PATH" "$INSTALL_TYPE"
    
    # アクティベーション
    activate_agents "$INSTALL_PATH" "$INSTALL_TYPE"
    
    echo ""
    echo "============================================================"
    echo -e "${GREEN}✅ インストール完了！${NC}"
    echo ""
    echo "使用方法:"
    echo "1. Claude Codeを起動: claude"
    echo "2. 以下のコマンドでAgent を呼び出し:"
    echo "   @spec-master-agent プロジェクトを開始します"
    echo ""
    echo "詳細は manual.md を参照してください。"
    echo "============================================================"
}

# 実行
main