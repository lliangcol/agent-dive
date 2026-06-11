# Ruflo Study Plan

## Learning Objectives

- Understand how Ruflo combines multi-agent swarm, MCP tools, memory, hooks and plugins into agent harnesses.
- Find boundaries for Claude Code plugin, CLI full install, Codex `.agents` config and Web UI.
- Verify Ruflo CLI, MCP server, init write scope and hook behavior.
- Summarize the designs that can be used for reference and those that cannot be copied.

## Stage arrangement

1. Document reading: README, package metadata, Claude plugin manifest, `.agents/config.toml`.
2. Read-only verification: `ruflo --version`, `ruflo --help`, `ruflo mcp start --help`, `ruflo init --help`.
3. source reading:wrapper, CLI/MCP entry, command registry, MCP tools, SwarmCoordinator, WorkflowEngine, HybridBackend.
4. Minimal integration: temporary project verification Claude plugin lite, CLI full init, MCP tool list, Codex `.agents`.
5. Comparison and review: Make boundary comparisons with ECC, CodeGraph, Graphify, and Caveman.

## Current boundary

This note does not yet contain any native run results. All commands require subsequent, individually logged output.
