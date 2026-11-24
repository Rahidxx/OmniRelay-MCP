⚡ OmniRelay MCP

Less Magic. More Utility.

Deterministic, Permission-Scoped Cross-App Workflows for Everyday Life.

<p align="center">
  <b>Turning fragmented everyday applications into structured, secure and human-approved AI workflows.</b>
</p><p align="center">
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![MCP](https://img.shields.io/badge/Model_Context_Protocol-111827?style=for-the-badge)
  ![AI](https://img.shields.io/badge/AI-Orchestration-8B5CF6?style=for-the-badge)
  ![Status](https://img.shields.io/badge/Status-Early_Prototype-orange?style=for-the-badge)
</p>---

🌐 Overview

OmniRelay MCP is a proposed local-first Model Context Protocol (MCP) orchestration hub designed to connect everyday applications through structured, verifiable and permission-controlled workflows.

Instead of relying on unpredictable AI actions, OmniRelay separates AI planning from actual execution using deterministic workflows and human approval.

🚨 The Problem

Everyday tasks are spread across multiple applications:

- Emails in Gmail
- Events in Google Calendar
- Documents in Drive
- Expenses in UPI and Splitwise
- Conversations in messaging apps

Users repeatedly switch between applications and manually transfer information.

Existing AI agents can also lack reliable execution controls and transparent permissions.

💡 Our Solution

OmniRelay MCP introduces a structured execution system with:

- Typed MCP servers and strict JSON schemas.
- Deterministic workflow orchestration.
- Human-in-the-Loop approval.
- Permission-based execution.
- Budget and action guardrails.
- Reusable automated routines.

🏗️ System Architecture

flowchart TD
    A["User Command"] --> B["Client Interface"]
    B --> C["AI Intent Planner"]
    C --> D["Schema Validation"]
    D --> E["Policy & Guardrail Engine"]
    E --> F{"Approval Required?"}
    F -->|Yes| G["Human Approval"]
    F -->|No| H["MCP Execution"]
    G --> H
    H --> I["Modular MCP Servers"]
    I --> J["Connected Applications"]
    J --> K["Execution Result & Audit Log"]

Four Core Layers

Layer| Responsibility
01. Client Interface| Commands and approval cards
02. Intent Planner| Converts requests into workflows
03. Guardrail Engine| Validates permissions and limits
04. MCP Servers| Connects external applications

✨ Key Features

🔗 Cross-App Orchestration

Connect multiple everyday services through structured workflows.

🛡️ Permission-Based Execution

Control which actions an AI agent can perform.

👤 Human-in-the-Loop

Require user approval before sensitive operations.

⚙️ Deterministic Workflows

Use validated execution steps instead of uncontrolled tool calls.

🔍 Execution Transparency

Maintain an audit trail of workflow actions.

🚀 Everyday Use Cases

1. Smart Bill & Split Autopilot

Gmail → Receipt Parser → Expense Split → UPI Link → Calendar Reminder

2. Appointment & Commute Sync

Email / Messaging → Calendar → Maps → Travel Reminder

3. Document & Deadline Concierge

PDF / Drive → Information Extraction → Tasks → Email Draft

🧰 Proposed Technology Stack

Component| Technology
Programming| Python
AI Orchestration| LangGraph
Validation| Pydantic
Protocol| Model Context Protocol
Database| SQLite
Frontend| Next.js
Integrations| Google Workspace APIs

🔐 Security by Design

- Permission-scoped operations.
- Human approval for sensitive actions.
- Monetary threshold checks.
- Duplicate-action prevention.
- Local-first data handling as an architectural goal.

🗺️ Development Roadmap

- [x] Project concept and problem definition
- [x] Technical architecture design
- [x] Initial policy-gate demonstration
- [ ] Core MCP server implementation
- [ ] Workflow orchestration
- [ ] Application integrations
- [ ] Approval interface
- [ ] End-to-end MVP

📌 Current Project Status

OmniRelay MCP is currently at the early prototype and architecture stage. The repository contains the project documentation and an initial policy-gate demonstration. Full MCP orchestration and external integrations are planned.

🏆 Hackathon

Event: wHACKiest 2026
Round: Round 1 – Ideathon
Track: T-1 – Make MCP Matter: Less Magic, More Utility

---

<p align="center">
  <b>OMNIRELAY MCP</b><br>
  Making AI execution structured, transparent and trustworthy.
</p>
