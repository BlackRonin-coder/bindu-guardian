# Bindu Guardian

Bindu Guardian is a governed defensive decision architecture for high-risk systems.

It is designed for environments where human safety, service continuity, and system integrity must all be protected at the same time.

## Core Idea

Most systems either react too late or respond too bluntly.

Bindu Guardian is designed to help institutions detect meaningful instability, distinguish noise from coordinated threat, respond proportionally, and explain why a given action was chosen.

## Intended Use Context

This architecture is aimed at continuity-critical environments such as:

- hospitals
- universities
- public agencies
- other high-risk institutional systems

## Public Repository Scope

This repository is a protected public release.

It shows the architectural model, operating logic at a high level, and example behavioural patterns.

It does not expose:

- protected internal decision logic
- scoring thresholds
- tuning methods
- proprietary optimisation heuristics
- sensitive implementation details

## Public Architecture Layers

- Signal Detection
- Correlation
- Trust Evaluation
- Deception Resistance
- Consensus
- Temporal Analysis
- Situation Classification
- Explainability

## Design Principles

- people first
- continuity where safely possible
- proportional response
- selective containment over blunt shutdown
- governed operation, not uncontrolled autonomy
- explainability and auditability

## Project Context

Bindu Guardian sits within a wider systems-design and governance context associated with Coal Tiger LTD.

See `docs/company.md` for company context and contact details.

## Documents

- `docs/architecture.md`
- `docs/examples.md`
- `docs/positioning.md`
- `docs/company.md`

## Public Note

This repository is for architectural presentation, evaluation, and communication.

It is not a full public release of the underlying protected implementation.


## Governance and Release Boundary

This repository is governed as a protected public release.

Additional public-governance documents:
- `SECURITY.md`
- `CONTRIBUTING.md`
- `docs/public_release_boundary.md`
