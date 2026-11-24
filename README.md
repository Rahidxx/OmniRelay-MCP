
# OmniRelay MCP

### Deterministic, Permission-Scoped Cross-App Workflows for Everyday Life

**Hackathon:** wHACKiest 2026  
**Track:** T-1 – Make MCP Matter: Less Magic, More Utility

## 1. Problem Statement

People use multiple applications for everyday activities such as emails, calendars, payments, documents and messaging.

Current AI agents often lack reliable cross-app coordination, strict permissions and user approval before important actions.

## 2. Proposed Solution

OmniRelay MCP is a local-first Model Context Protocol orchestration hub designed to connect everyday applications through structured and verifiable workflows.

## 3. Key Features

- Typed MCP Servers with strict JSON schemas.
- Deterministic workflow execution.
- Human-in-the-Loop approval for important actions.
- Permission and budget-based guardrails.
- Reusable automated routines.
- Local-first data handling.

## 4. Technical Architecture

1. Client Interface – User commands and approval cards.
2. Intent & Planner – Converts requests into structured workflows.
3. Policy & Guardrail Engine – Validates permissions and limits.
4. Modular MCP Servers – Connects external applications and services.

## 5. Main Use Cases

### Smart Bill & Split Autopilot
Processes receipts, calculates shared expenses and prepares payment links.

### Appointment & Commute Sync
Coordinates appointments, calendars and travel reminders.

### Document & Deadline Concierge
Extracts important information from documents and prepares reminders.

## 6. Technology Stack (Planned)

- Python
- Model Context Protocol (MCP)
- LangGraph
- Pydantic
- SQLite
- Next.js
- Google Workspace APIs

## 7. Project Status

This repository currently contains the project concept and architecture documentation. The working MVP and external integrations are planned for development.

## 8. Hackathon

Submitted for wHACKiest 2026 – Round 1 Ideathon.

**Project:** OmniRelay MCP
**Track:** T-1

