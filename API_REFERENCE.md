# API Reference - APIリファレンス

*バージョン: v2.0.0*
*最終更新: 2025年01月25日 00:30 JST*

## 📌 概要

Spec Agent System の各エージェントのインターフェース仕様、入出力フォーマット、カスタマイズポイントを詳細に説明します。

## 📚 目次

1. [共通インターフェース](#共通インターフェース)
2. [エージェント別API](#エージェント別api)
3. [データフォーマット](#データフォーマット)
4. [カスタマイズAPI](#カスタマイズapi)
5. [イベントシステム](#イベントシステム)
6. [エラーハンドリング](#エラーハンドリング)

---

## 🔧 共通インターフェース

### 基本構造

すべてのエージェントは以下の共通インターフェースを実装しています：

```typescript
interface Agent {
  name: string;
  version: string;
  description: string;
  
  // メソッド
  initialize(): Promise<void>;
  execute(input: AgentInput): Promise<AgentOutput>;
  validate(input: any): ValidationResult;
  terminate(): Promise<void>;
}
```

### 共通入力フォーマット

```json
{
  "agent": "agent-name",
  "action": "action-type",
  "context": {
    "project_id": "uuid",
    "session_id": "uuid",
    "user_id": "uuid"
  },
  "parameters": {
    // エージェント固有のパラメータ
  },
  "options": {
    "timeout": 30000,
    "verbose": false,
    "format": "markdown"
  }
}
```

### 共通出力フォーマット

```json
{
  "status": "success | error | warning",
  "agent": "agent-name",
  "timestamp": "2025-01-25T00:30:00Z",
  "data": {
    // エージェント固有の出力データ
  },
  "metadata": {
    "execution_time": 1234,
    "tokens_used": 5678
  },
  "errors": [],
  "warnings": []
}
```

---

## 🤖 エージェント別API

### 1. spec-master-agent

#### 初期化

```javascript
// 入力
{
  "agent": "spec-master-agent",
  "action": "initialize",
  "parameters": {
    "project_name": "My Awesome Project",
    "project_type": "web_application",
    "methodology": "waterfall | agile | hybrid"
  }
}

// 出力
{
  "status": "success",
  "data": {
    "project_id": "550e8400-e29b-41d4-a716-446655440000",
    "created_files": [
      "progress.md",
      "todo.md",
      "specifications/"
    ],
    "workflow": {
      "phases": ["requirement", "design", "implementation", "review"],
      "current_phase": "requirement"
    }
  }
}
```

#### 進捗管理

```javascript
// 入力
{
  "agent": "spec-master-agent",
  "action": "update_progress",
  "parameters": {
    "phase": "requirement",
    "progress": 75,
    "completed_tasks": ["task1", "task2"],
    "pending_tasks": ["task3"]
  }
}

// 出力
{
  "status": "success",
  "data": {
    "overall_progress": 25,
    "phase_progress": {
      "requirement": 75,
      "design": 0,
      "implementation": 0,
      "review": 0
    },
    "estimated_completion": "2025-02-01"
  }
}
```

### 2. requirement-analyst-agent

#### 要求分析

```javascript
// 入力
{
  "agent": "requirement-analyst-agent",
  "action": "analyze",
  "parameters": {
    "input_type": "text | document | interview",
    "content": "ECサイトを作りたい。商品管理、在庫管理、決済機能が必要。",
    "analysis_depth": "basic | detailed | comprehensive"
  }
}

// 出力
{
  "status": "success",
  "data": {
    "functional_requirements": [
      {
        "id": "FR001",
        "category": "商品管理",
        "description": "商品の登録、編集、削除機能",
        "priority": "high",
        "acceptance_criteria": [
          "商品情報の CRUD 操作が可能",
          "画像アップロード機能",
          "カテゴリ分類機能"
        ]
      }
    ],
    "non_functional_requirements": [
      {
        "id": "NFR001",
        "category": "パフォーマンス",
        "description": "ページ表示速度",
        "criteria": "3秒以内",
        "measurement": "95パーセンタイル"
      }
    ],
    "use_cases": [
      {
        "id": "UC001",
        "name": "商品購入",
        "actors": ["購入者", "システム"],
        "flow": ["商品選択", "カート追加", "決済", "確認"]
      }
    ]
  }
}
```

### 3. system-architect-agent

#### アーキテクチャ設計

```javascript
// 入力
{
  "agent": "system-architect-agent",
  "action": "design",
  "parameters": {
    "requirements": ["requirement_ids"],
    "architecture_style": "monolithic | microservices | serverless",
    "constraints": {
      "budget": "medium",
      "timeline": "3_months",
      "team_size": 5
    }
  }
}

// 出力
{
  "status": "success",
  "data": {
    "architecture": {
      "type": "microservices",
      "components": [
        {
          "name": "API Gateway",
          "technology": "Kong",
          "responsibility": "ルーティング、認証",
          "interfaces": ["REST", "GraphQL"]
        }
      ],
      "data_flow": {
        "diagram": "mermaid_code_here"
      }
    },
    "technology_stack": {
      "frontend": ["React", "TypeScript"],
      "backend": ["Node.js", "Python"],
      "database": ["PostgreSQL", "Redis"],
      "infrastructure": ["AWS", "Docker", "Kubernetes"]
    },
    "deployment": {
      "strategy": "blue_green",
      "environments": ["dev", "staging", "production"]
    }
  }
}
```

### 4. implementation-spec-agent

#### API仕様定義

```javascript
// 入力
{
  "agent": "implementation-spec-agent",
  "action": "define_api",
  "parameters": {
    "api_style": "rest | graphql | grpc",
    "endpoints": [
      {
        "resource": "products",
        "operations": ["GET", "POST", "PUT", "DELETE"]
      }
    ],
    "authentication": "jwt | oauth2 | api_key"
  }
}

// 出力
{
  "status": "success",
  "data": {
    "openapi": "3.0.0",
    "info": {
      "title": "Product API",
      "version": "1.0.0"
    },
    "paths": {
      "/products": {
        "get": {
          "summary": "商品一覧取得",
          "parameters": [
            {
              "name": "page",
              "in": "query",
              "schema": { "type": "integer" }
            }
          ],
          "responses": {
            "200": {
              "description": "成功",
              "content": {
                "application/json": {
                  "schema": {
                    "$ref": "#/components/schemas/ProductList"
                  }
                }
              }
            }
          }
        }
      }
    },
    "components": {
      "schemas": {
        "Product": {
          "type": "object",
          "properties": {
            "id": { "type": "string", "format": "uuid" },
            "name": { "type": "string" },
            "price": { "type": "number" }
          }
        }
      }
    }
  }
}
```

### 5. technical-writer-agent

#### ドキュメント整形

```javascript
// 入力
{
  "agent": "technical-writer-agent",
  "action": "format",
  "parameters": {
    "documents": ["requirement_spec.md", "api_spec.md"],
    "format_rules": {
      "style_guide": "microsoft | google | custom",
      "language": "ja | en | both",
      "terminology": {
        "user": "ユーザー",
        "login": "サインイン"
      }
    },
    "output_format": "markdown | html | pdf"
  }
}

// 出力
{
  "status": "success",
  "data": {
    "formatted_documents": [
      {
        "name": "requirement_spec_formatted.md",
        "changes": [
          {
            "type": "terminology",
            "before": "ユーザ",
            "after": "ユーザー",
            "count": 15
          }
        ]
      }
    ],
    "statistics": {
      "total_changes": 42,
      "readability_score": 85,
      "consistency_score": 95
    }
  }
}
```

### 6. qa-reviewer-agent

#### 品質レビュー

```javascript
// 入力
{
  "agent": "qa-reviewer-agent",
  "action": "review",
  "parameters": {
    "documents": ["all"],
    "review_criteria": {
      "completeness": true,
      "consistency": true,
      "technical_accuracy": true,
      "best_practices": true
    },
    "severity_threshold": "low | medium | high"
  }
}

// 出力
{
  "status": "success",
  "data": {
    "review_summary": {
      "score": 78,
      "grade": "B",
      "total_issues": 12,
      "critical_issues": 2
    },
    "issues": [
      {
        "id": "ISSUE001",
        "severity": "high",
        "category": "security",
        "location": "api_spec.md:L125",
        "description": "認証なしでアクセス可能なエンドポイント",
        "recommendation": "JWT認証を追加"
      }
    ],
    "improvements": [
      {
        "area": "performance",
        "current": "未定義",
        "suggested": "レスポンスタイム目標を設定"
      }
    ]
  }
}
```

---

## 📊 データフォーマット

### プロジェクト設定

```yaml
# .claude/project.yaml
project:
  name: "My Project"
  version: "1.0.0"
  agents:
    enabled:
      - spec-master-agent
      - requirement-analyst-agent
      - system-architect-agent
    disabled: []
  
  settings:
    language: ja
    output_format: markdown
    auto_save: true
    
  workflow:
    type: waterfall
    phases:
      - name: requirement
        duration: 5
        agents: [requirement-analyst-agent]
      - name: design
        duration: 7
        agents: [system-architect-agent]
```

### 進捗データ

```json
{
  "project_id": "uuid",
  "timestamp": "2025-01-25T00:30:00Z",
  "phases": [
    {
      "name": "requirement",
      "status": "in_progress",
      "progress": 75,
      "started_at": "2025-01-20T09:00:00Z",
      "completed_at": null,
      "tasks": [
        {
          "id": "TASK001",
          "name": "ユーザーインタビュー",
          "status": "completed",
          "assignee": "requirement-analyst-agent"
        }
      ]
    }
  ],
  "overall_progress": 25,
  "estimated_completion": "2025-02-15T17:00:00Z"
}
```

---

## 🎨 カスタマイズAPI

### カスタムエージェント作成

```javascript
class CustomAgent extends BaseAgent {
  constructor(config) {
    super(config);
    this.name = 'custom-agent';
    this.version = '1.0.0';
  }
  
  async execute(input) {
    // バリデーション
    const validation = this.validate(input);
    if (!validation.valid) {
      throw new ValidationError(validation.errors);
    }
    
    // カスタム処理
    const result = await this.process(input.parameters);
    
    // 出力フォーマット
    return this.formatOutput(result);
  }
  
  async process(params) {
    // カスタムロジック
    return {
      custom_data: 'processed'
    };
  }
}

// 登録
AgentRegistry.register(new CustomAgent({
  config_path: './custom-agent.yaml'
}));
```

### フックシステム

```javascript
// フック登録
Hooks.register('before_execute', async (agent, input) => {
  console.log(`Executing ${agent.name} with`, input);
  // カスタム前処理
});

Hooks.register('after_execute', async (agent, output) => {
  // カスタム後処理
  await saveToDatabase(output);
});

// フック実行
await Hooks.trigger('before_execute', [agent, input]);
```

### プラグインシステム

```javascript
// プラグイン定義
export class TranslationPlugin {
  name = 'translation-plugin';
  version = '1.0.0';
  
  async install(agent) {
    agent.addMethod('translate', this.translate.bind(this));
  }
  
  async translate(text, targetLang) {
    // 翻訳処理
    return translatedText;
  }
}

// プラグイン使用
agent.use(new TranslationPlugin());
const translated = await agent.translate('Hello', 'ja');
```

---

## 📡 イベントシステム

### イベント一覧

| イベント名 | 説明 | パラメータ |
|-----------|------|-----------|
| `agent.initialized` | エージェント初期化完了 | `{ agent, config }` |
| `agent.executing` | 実行開始 | `{ agent, input }` |
| `agent.completed` | 実行完了 | `{ agent, output }` |
| `agent.error` | エラー発生 | `{ agent, error }` |
| `progress.updated` | 進捗更新 | `{ phase, progress }` |
| `document.created` | ドキュメント作成 | `{ path, content }` |
| `review.completed` | レビュー完了 | `{ issues, score }` |

### イベントリスナー

```javascript
// イベントリスナー登録
EventBus.on('agent.completed', (event) => {
  console.log(`Agent ${event.agent.name} completed`);
  updateDashboard(event.output);
});

// カスタムイベント発行
EventBus.emit('custom.event', {
  type: 'notification',
  message: 'Custom event triggered'
});

// 一度だけ実行
EventBus.once('agent.initialized', (event) => {
  console.log('First initialization');
});
```

---

## ⚠️ エラーハンドリング

### エラーコード体系

| コード | 名称 | 説明 | 対処法 |
|--------|------|------|--------|
| `E001` | `AGENT_NOT_FOUND` | エージェントが見つからない | エージェント名を確認 |
| `E002` | `INVALID_INPUT` | 入力パラメータが不正 | パラメータ形式を確認 |
| `E003` | `TIMEOUT` | 処理タイムアウト | タイムアウト値を増やす |
| `E004` | `PERMISSION_DENIED` | アクセス権限なし | 権限設定を確認 |
| `E005` | `RESOURCE_NOT_FOUND` | リソースが存在しない | ファイルパスを確認 |
| `E006` | `VALIDATION_ERROR` | バリデーションエラー | 入力値を修正 |
| `E007` | `PROCESSING_ERROR` | 処理中のエラー | ログを確認 |

### エラーレスポンス形式

```json
{
  "status": "error",
  "error": {
    "code": "E002",
    "message": "Invalid input parameters",
    "details": {
      "field": "parameters.project_name",
      "reason": "Required field missing"
    },
    "timestamp": "2025-01-25T00:30:00Z",
    "trace_id": "abc-123-def"
  },
  "suggestions": [
    "Add 'project_name' to parameters",
    "Check API documentation for required fields"
  ]
}
```

### エラーハンドリング例

```javascript
try {
  const result = await agent.execute(input);
  return result;
} catch (error) {
  if (error.code === 'E002') {
    // バリデーションエラーの処理
    console.error('Validation failed:', error.details);
    return createValidationResponse(error);
  } else if (error.code === 'E003') {
    // タイムアウトの処理
    console.warn('Operation timed out, retrying...');
    return retryWithBackoff(agent, input);
  } else {
    // その他のエラー
    console.error('Unexpected error:', error);
    throw error;
  }
}
```

---

## 🔒 セキュリティ

### 認証・認可

```javascript
// API キー認証
const auth = new ApiKeyAuth({
  header: 'X-API-Key',
  validate: async (key) => {
    return await validateApiKey(key);
  }
});

// JWT 認証
const jwtAuth = new JWTAuth({
  secret: process.env.JWT_SECRET,
  algorithm: 'HS256',
  expiresIn: '1h'
});

// 使用例
agent.use(auth.middleware());
```

### データ暗号化

```javascript
// 設定
{
  "security": {
    "encryption": {
      "enabled": true,
      "algorithm": "AES-256-GCM",
      "key_rotation": "30d"
    },
    "data_masking": {
      "enabled": true,
      "fields": ["password", "api_key", "credit_card"]
    }
  }
}
```

---

## 📈 パフォーマンス最適化

### キャッシング

```javascript
// キャッシュ設定
const cache = new Cache({
  store: 'redis',
  ttl: 3600,
  max_size: '100MB'
});

// キャッシュ使用
const cachedResult = await cache.get('requirement_analysis');
if (!cachedResult) {
  const result = await agent.analyze(input);
  await cache.set('requirement_analysis', result);
  return result;
}
return cachedResult;
```

### バッチ処理

```javascript
// バッチ実行
const batch = new BatchProcessor({
  size: 10,
  timeout: 5000
});

batch.add(agent1.execute(input1));
batch.add(agent2.execute(input2));
batch.add(agent3.execute(input3));

const results = await batch.execute();
```

---

## 🔗 関連リンク

- [Usage Guide](USAGE.md) - 使用ガイド
- [Installation](INSTALLATION.md) - インストール手順
- [Contributing](CONTRIBUTING.md) - 開発参加方法
- [GitHub API Docs](https://github.com/KEIEI-NET/spec-agent/wiki/API)

---

*最終更新: 2025年01月25日 00:30 JST*
*バージョン: v2.0.0*

**更新履歴:**
- v2.0.0 (2025年01月25日): 初版作成、全エージェントのAPI仕様定義