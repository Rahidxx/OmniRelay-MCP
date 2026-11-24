⚡ OmniRelay MCP

Less Magic. More Utility.

Deterministic, Permission-Scoped Cross-App Workflows for Everyday Life.

<p align="center">
  <img src="https://img.shields.io/badge/Project-OmniRelay_MCP-6366f1?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Protocol-MCP-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Early_Prototype-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Track-MAKE_MCP_MATTER-purple?style=for-the-badge" />
</p>---

◈ 01. Project Overview

OmniRelay MCP is a proposed local-first orchestration hub designed to connect everyday applications through structured, verifiable, and permission-controlled workflows.

Instead of relying on disconnected AI actions, OmniRelay introduces a deterministic execution architecture where every workflow follows defined steps, validates permissions, and requests human approval before sensitive operations.

Core Philosophy: AI-assisted planning. Deterministic execution. Human-controlled actions.

◈ 02. The Problem

Modern digital workflows are fragmented across multiple applications.

- Application silos create disconnected workflows.
- Repetitive manual operations waste time.
- Uncontrolled AI actions introduce reliability concerns.
- Limited permission transparency creates security risks.

◈ 03. The Solution

OmniRelay MCP proposes a modular orchestration layer built around four core capabilities:

Capability| Function
Typed MCP Interfaces| Structured tool communication
Workflow Orchestration| Defined execution sequences
Policy Enforcement| Permission and action validation
Human-in-the-Loop| Approval before sensitive actions

◈ 04. System Architecture

flowchart TD
    A["USER INTERFACE"] --> B["INTENT & PLANNER"]
    B --> C["POLICY & GUARDRAIL ENGINE"]
    C --> D{"APPROVAL REQUIRED?"}
    D -->|Yes| E["HUMAN APPROVAL"]
    E --> F["WORKFLOW EXECUTION"]
    D -->|No| F
    F --> G["MCP SERVER LAYER"]
    G --> H["WORKSPACE"]
    G --> I["LOCAL FILES"]
    G --> J["FINANCE"]
    G --> K["COMMUNICATION & GEO"]
    H --> L["EXECUTION RESULT"]
    I --> L
    J --> L
    K --> L

Architecture Layers

01 — Client Interface

- User commands
- Workflow visibility
- Approval interaction

02 — Intent & Planner

- Intent interpretation
- Schema-constrained planning
- Workflow decomposition

03 — Policy & Guardrail Engine

- Role-based access control
- Permission validation
- Action thresholds
- Approval requirements

04 — Modular MCP Servers

- Workspace integrations
- Local file operations
- Finance and expense workflows
- Communication and location services

◈ 05. Core Use Cases

1. Smart Bill & Split Autopilot

"Gmail → Receipt Extraction → Expense Split → Approval"

Automates the proposed flow of identifying bills, extracting expense information, and preparing expense-sharing actions.

2. Appointment & Commute Sync

"Messages → Calendar → Maps → Reminder"

Connects appointment information with calendar scheduling and commute planning.

3. Document & Deadline Concierge

"Documents → Data Extraction → Task Planning → Email Draft"

Transforms document information into organised tasks, deadlines, and follow-up drafts.

◈ 06. Proposed Technology Stack

Layer| Technology
Core Development| Python
Tool Communication| Model Context Protocol
Workflow Orchestration| LangGraph
Data Validation| Pydantic
Local Storage| SQLite
Frontend| Next.js
Document Processing| PyMuPDF
AI Planning| Claude / Gemini

These are proposed technologies for the planned implementation, not a claim that all integrations are currently operational.

◈ 07. Repository Structure

OmniRelay-MCP/
│
├── README.md
├── policy_gate.py
├── requirements.txt
│
├── docs/
│   ├── architecture.md
│   └── use-cases.md
│
├── src/
│   ├── planner/
│   ├── guardrails/
│   └── mcp_servers/
│
└── assets/
    ├── presentation/
    └── demo/

◈ 08. Security & Reliability Principles

- Permission-Scoped Execution: Actions should operate within authorised boundaries.
- Human Approval: Sensitive operations should require explicit user confirmation.
- Structured Validation: Typed schemas help validate inputs and outputs.
- Deterministic Workflows: Defined execution steps improve predictability.
- Modular Design: Independent server modules support extensibility.

◈ 09. Development Roadmap

- [x] Project concept and architecture
- [x] Initial policy-gate demonstration
- [ ] Core MCP server implementation
- [ ] Workflow orchestration engine
- [ ] External application integrations
- [ ] Human approval interface
- [ ] End-to-end workflow testing

◈ 10. Current Implementation Status

This repository currently contains project documentation and an initial Python policy-gate prototype.

The complete orchestration engine, external integrations, and approval interface remain planned development components.

◈ 11. Project Presentation

Project: OmniRelay MCP
Hackathon: wHACKiest 2026
Track: MAKE MCP MATTER — LESS MAGIC, MORE UTILITY

---

<p align="center">
  <b>OMNIRELAY MCP</b><br/>
  <i>Connect Applications. Control Actions. Simplify Workflows.</i>
</p>
