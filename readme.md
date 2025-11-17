# Legacy Rules Modernization – Micro-Solution Demo

## Context

Legacy PL/SQL rules are widely used in corporate environments for eligibility and policy decisions.

## Problem

- Rules are implicit and order-dependent
- No decision explainability
- Hard to integrate with APIs or AI systems
- High operational risk during rule changes

## Solution

This demo shows how legacy PL/SQL rules can be:

- Refactored into clean Python logic
- Made explainable with decision traces
- Exposed via REST API
- Containerized using Docker

## Usefulness

- Gradual modernization initiatives
- Legacy system offloading
- Audit and compliance requirements
- AI-ready decision pipelines

## Showcasing

- Technical refactoring approach
- Clear separation of concerns
- Representative, non-production example

## How to run

```bash
docker compose build

docker compose up --build

Seed demo data:

POST http://localhost:8000/seed


Evaluate:

GET http://localhost:8000/evaluate/1

The Transformation
Legacy (PL/SQL Example):

SQL
IF v_usage > 600 THEN
   o_eligible := 'N';
END IF;
Modernized (Python):

Python
if customer.monthly_usage > 600:
    eligible = False
    decisions.append("Rejected: monthly usage above 600")
```
