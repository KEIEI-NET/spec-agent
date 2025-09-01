# CLAUDE.md - Claude Code Integration Guide

*Version: v2.0.0*
*Last Updated: 2025-01-25 00:30 JST*

This file provides comprehensive guidance to Claude Code (claude.ai/code) when working with the Spec Agent System repository.

## 📌 Project Overview

Spec Agent System is a sophisticated Japanese-language specification document generation framework utilizing multiple specialized AI agents. The system orchestrates 6 expert agents to create comprehensive, production-ready software specifications through a structured workflow from initial requirements to detailed implementation specifications.

### Key Characteristics
- **Language**: Primary documentation in Japanese, code comments in English
- **Architecture**: Multi-agent collaborative system
- **Integration**: Native Claude Code CLI sub-agent system
- **Methodology**: Supports waterfall, agile, and hybrid approaches

## 🏗️ Agent System Architecture

The system consists of 6 specialized agents coordinated through YAML rules:

1. **spec-master-agent.md** - Master coordinator managing the entire specification process
2. **requirement-analyst-agent.md** - Requirements analysis and validation
3. **system-architect-agent.md** - System architecture and data model design
4. **implementation-spec-agent.md** - Implementation details, API specs, and test specifications
5. **technical-writer-agent.md** - Document formatting and consistency
6. **qa-reviewer-agent.md** - Quality review and validation

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
# Initialize new project
@spec-master-agent initialize project "Project Name"

# Start requirement analysis
@requirement-analyst-agent analyze requirements

# Generate architecture
@system-architect-agent design architecture

# Create implementation specs
@implementation-spec-agent define implementation

# Format all documents
@technical-writer-agent format all

# Run quality review
@qa-reviewer-agent review specifications
```

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

*Last Updated: 2025-01-25 00:30 JST*
*Version: v2.0.0*

**Update History:**
- v2.0.0 (2025-01-25): Complete overhaul with Claude Code specific instructions, added integration guidelines