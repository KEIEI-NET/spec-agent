# CLAUDE.md - Claude Code Integration Guide

*Version: v1.1.0*
*Last Updated: 2025-09-01 18:25 JST*

This file provides comprehensive guidance to Claude Code (claude.ai/code) when working with the Spec Agent After repository.

## 📌 Project Overview

Spec Agent After は、自動車アフターマーケット業界に特化した仕様書自動作成システムです。部品商社、ガラス専門、リサイクルの各セクターに対応し、国内外全メーカー（トヨタ、日産、ホンダ、三菱、マツダ、スバル、ダイハツ、スズキ、BMW、メルセデス、アウディ等）の部品管理仕様書を生成します。

### Key Characteristics
- **Industry**: 自動車アフターマーケット業界特化
- **Coverage**: 全メーカー対応（国産8社、商用車4社、欧州車5社以上）
- **Architecture**: セクター別マルチエージェントシステム
- **Integration**: Claude Code CLI ネイティブ統合
- **Compliance**: 法規制準拠（PL法、IATF 16949、道路運送車両法等）

## 🏗️ Agent System Architecture

### Core Agents (基本エージェント - 7個)
1. **auto-spec-master-agent.md** - 統括管理
2. **auto-requirement-agent.md** - 要求分析
3. **auto-system-architect-agent.md** - システム設計
4. **auto-implementation-agent.md** - 実装仕様
5. **auto-integration-agent.md** - 統合仕様
6. **auto-qa-reviewer-agent.md** - 品質レビュー
7. **auto-compliance-agent.md** - コンプライアンス

### Sector-Specific Agents (セクター別エージェント - 11個)

#### 部品商社セクター（5エージェント）
- **parts-catalog-agent.md** - 部品カタログ管理
- **inventory-forecast-agent.md** - 在庫予測
- **compliance-verification-agent.md** - コンプライアンス検証
- **commercial-vehicle-parts-agent.md** - 大型車両部品管理 🆕
- **european-vehicle-parts-agent.md** - 欧州車部品管理 🆕

#### ガラス専門セクター（3エージェント）
- **adas-calibration-agent.md** - ADAS校正
- **glass-specification-agent.md** - ガラス仕様管理
- **insurance-integration-agent.md** - 保険連携

#### リサイクルセクター（3エージェント）
- **dismantling-process-agent.md** - 解体工程管理
- **circular-economy-agent.md** - 循環経済支援
- **manifest-management-agent.md** - マニフェスト管理

## 📁 Key Files and Their Purpose

- `coordination_rules.yaml` - Defines workflow and communication rules between agents
- `progress.md` - Tracks overall project progress through phases
- `todo.md` - Task management with priority levels
- `manual.md` - Comprehensive user manual for the agent system
- `specifications/` - Directory for generated specification documents (to be created)

## 🔄 Workflow Phases

1. **要求分析 (Requirements Analysis)** - Gather and document functional/non-functional requirements
2. **システム設計 (System Design)** - Create architecture and data models
3. **実装仕様 (Implementation Specs)** - Define APIs, modules, and coding standards
4. **ドキュメント整形 (Documentation)** - Format and ensure consistency
5. **品質レビュー (Quality Review)** - Validate completeness and correctness

## 📂 Expected Output Structure

```
specifications/
├── requirement_spec.md     # Requirements specification
├── architecture_design.md  # System architecture
├── data_model.md           # Database design
├── implementation_spec.md  # Implementation details
├── api_spec.md            # API specifications
├── test_spec.md           # Test specifications
├── coding_standards.md    # Coding conventions
└── review_report.md       # Quality review results
```

## ⚠️ Important Notes for Claude Code

### Language Guidelines
- **Documentation**: Japanese (with English headers for navigation)
- **Code Comments**: English for international compatibility
- **User Interaction**: Japanese preferred, English supported
- **Error Messages**: Bilingual (Japanese primary, English secondary)

### Technical Constraints
- **File Encoding**: UTF-8 mandatory
- **Line Endings**: LF (Unix-style) preferred
- **Path Separators**: Use forward slashes even on Windows
- **Max File Size**: Keep individual specs under 100KB

### Agent Communication Protocol
- Agents communicate via structured markdown files
- Each agent must validate input before processing
- Output must conform to predefined schemas
- Error handling must be graceful with fallbacks

### Development Best Practices
1. **Atomic Operations**: Each agent action should be atomic
2. **Idempotency**: Repeated operations should produce same result
3. **Validation**: Always validate inputs and outputs
4. **Logging**: Maintain detailed logs in progress.md
5. **Version Control**: Track all specification versions

## 🔧 Claude Code Specific Instructions

### When Creating Specifications
1. Always start with `@spec-master-agent` for coordination
2. Maintain progress.md and todo.md continuously
3. Create specifications/ directory if not exists
4. Use relative paths within project directory
5. Preserve existing files unless explicitly updating

### Error Recovery
```javascript
try {
  // Agent operation
} catch (error) {
  // Log to progress.md
  // Attempt graceful recovery
  // Notify user with actionable message
}
```

### Performance Optimization
- Cache frequently accessed specifications
- Batch similar operations
- Minimize file I/O operations
- Use streaming for large documents

## 🚀 Quick Start Commands

```bash
# 統括エージェントで開始
@auto-spec-master-agent 部品管理システムの仕様書を作成

# セクター別エージェント呼び出し
@parts-catalog-agent 全メーカー対応の部品カタログ仕様
@commercial-vehicle-parts-agent いすゞ・日野対応の大型車両部品管理
@european-vehicle-parts-agent BMW・ベンツ対応の欧州車部品管理

# ガラス専門
@adas-calibration-agent ADAS校正システム仕様

# リサイクル
@dismantling-process-agent 解体工程管理システム仕様
```

## 🚗 Supported Manufacturers

### 国産車メーカー
- トヨタ/レクサス
- 日産/インフィニティ  
- ホンダ/アキュラ
- 三菱
- マツダ
- スバル
- ダイハツ
- スズキ

### 商用車メーカー
- いすゞ
- 日野
- 三菱ふそう
- UDトラックス

### 欧州車メーカー
- BMW/MINI
- メルセデスベンツ
- アウディ
- フォルクスワーゲン
- ポルシェ

## 📊 Metrics and Monitoring

Track these metrics in progress.md:
- Phase completion percentage
- Document word count
- Review issues found/resolved
- Time spent per phase
- Agent utilization rate

## 🔗 Integration Points

### With Version Control
- Auto-commit after each phase completion
- Tag releases with version numbers
- Branch for experimental specifications

### With CI/CD
- Trigger reviews on specification updates
- Generate PDF/HTML from markdown
- Deploy documentation to wiki/portal

### With Project Management
- Sync todo.md with issue trackers
- Update progress in PM tools
- Send notifications on milestones

---

*Last Updated: 2025-09-01 18:25 JST*
*Version: v1.1.0*

**Update History:**
- v1.1.0 (2025-09-01): 自動車アフターマーケット業界特化版に更新、全メーカー対応
- v1.0.0 (2025-01-25): 初版リリース