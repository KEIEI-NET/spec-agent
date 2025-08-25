# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Japanese-language specification document generation system using multiple specialized agents. The system orchestrates 6 different agents to create comprehensive software specifications from requirements through implementation details.

## Agent System Architecture

The system consists of 6 specialized agents coordinated through YAML rules:

1. **spec-master-agent.md** - Master coordinator managing the entire specification process
2. **requirement-analyst-agent.md** - Requirements analysis and validation
3. **system-architect-agent.md** - System architecture and data model design
4. **implementation-spec-agent.md** - Implementation details, API specs, and test specifications
5. **technical-writer-agent.md** - Document formatting and consistency
6. **qa-reviewer-agent.md** - Quality review and validation

## Key Files and Their Purpose

- `coordination_rules.yaml` - Defines workflow and communication rules between agents
- `progress.md` - Tracks overall project progress through phases
- `todo.md` - Task management with priority levels
- `manual.md` - Comprehensive user manual for the agent system
- `specifications/` - Directory for generated specification documents (to be created)

## Workflow Phases

1. **要求分析 (Requirements Analysis)** - Gather and document functional/non-functional requirements
2. **システム設計 (System Design)** - Create architecture and data models
3. **実装仕様 (Implementation Specs)** - Define APIs, modules, and coding standards
4. **ドキュメント整形 (Documentation)** - Format and ensure consistency
5. **品質レビュー (Quality Review)** - Validate completeness and correctness

## Expected Output Structure

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

## Important Notes

- All documentation and interactions are in Japanese
- Agents communicate through structured markdown files
- Progress tracking uses checkbox-based task lists
- The system follows a waterfall-like approach with feedback loops
- Each agent has specific deliverables defined in their respective .md files