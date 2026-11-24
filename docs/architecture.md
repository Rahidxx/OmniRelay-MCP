# OmniRelay MCP – System Architecture

## Overview
OmniRelay MCP is a proposed local-first orchestration hub designed to connect multiple applications through structured MCP workflows.

## Architecture Components

### 1. Client Interface
Provides a simple interface for users to initiate workflows and review approval requests.

### 2. Intent and Planner
Converts user requests into structured workflow steps using schema-constrained AI planning.

### 3. Policy and Guardrail Engine
Checks permissions, validates actions, and requests human approval before sensitive operations.

### 4. Modular MCP Servers
Connects supported services through separate MCP server modules.

Planned integrations include:
- Google Workspace
- Local Files
- Finance and Expenses
- Communication and Maps

## Workflow
1. User submits a request.
2. Planner identifies the required actions.
3. Policy engine validates permissions.
4. User approval is requested when necessary.
5. Approved actions are executed through the relevant MCP servers.
6. Results are returned to the user.

## Design Principles
- Permission-based execution
- Human-in-the-loop approval
- Structured data validation
- Modular architecture
- Local-first approach

## Current Status
This repository contains the project documentation and an initial policy-gate prototype. Full integrations and orchestration components are planned.
