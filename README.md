# F147 | Agentic Defense Policy Analyst | L3 Gold Standard | v1.0

A governed five-agent reference architecture for high-level defense-policy analysis across source review, capability context, policy options, legal and ethical constraints, civilian protection, strategic risk, uncertainty, provenance, and qualified human policy review.

F147 is deliberately limited to policy-level and strategic analysis. It does not provide operational targeting, weapon construction, weapon employment instructions, tactical evasion, operational command, or other actionable harm-enabling assistance. It cannot authorize force, approve operational plans, select targets, authorize weapon employment, issue operational commands, or distribute operational instructions.

## Defense-policy analysis lifecycle

```text
Question and Decision Context
        -> Source and Evidence Review
        -> Capability and Strategic Context
        -> Policy Options and Alternatives
        -> Legal, Ethical, Civilian-Protection Review
        -> Escalation, Strategic, and Implementation Risk
        -> Qualified Policy Approval
        -> Human-Controlled Policy Decision
```

The workflow fails closed when required reviews are missing or when material source, classification, operationalization, legal, ethical, civilian-harm, escalation, analytic-bias, or provenance issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Source Agent | Organizes public and authorized sources, provenance, freshness, corroboration, confidence, assumptions, gaps, and contradictions | What is actually supported by the evidence? |
| Capability Agent | Structures high-level capability context, readiness concepts, dependencies, constraints, industrial capacity, resilience, and strategic implications without operational employment detail | What capability context matters for the policy question? |
| Policy Agent | Develops policy objectives, alternatives, tradeoffs, implementation considerations, stakeholders, and reversible decision paths | What legitimate policy options exist and what are their tradeoffs? |
| Legal and Ethics Agent | Reviews authority, domestic and international legal context, human rights, civilian protection, ethics, oversight, and unresolved questions | What legal, ethical, and civilian-protection constraints require qualified review? |
| Risk Agent | Reviews escalation, deterrence, misperception, alliance effects, proliferation, strategic stability, second-order effects, uncertainty, and failure modes | What risks could make a seemingly attractive policy option dangerous or counterproductive? |

Agents support high-level defense-policy research, strategic studies, governance analysis, capability-policy review, oversight, academic research, public-sector analysis, and decision-support preparation. They do not replace lawful authorities, military command, intelligence authorities, legal counsel, elected officials, or qualified policy professionals.

## Repository structure

```text
AGENTS/
├── source_agent.py
├── capability_agent.py
├── policy_agent.py
├── legal_ethics_agent.py
└── risk_agent.py

SKILLS/
├── source_reasoning.py
├── capability_reasoning.py
├── policy_reasoning.py
├── legal_ethics_reasoning.py
└── risk_reasoning.py

TOOLS/
├── source_registry.py
├── assumption_log.py
├── options_matrix.py
├── risk_register.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Policy question framing

Analysis begins by defining the policy question, decision maker, jurisdiction, time horizon, strategic objective, stakeholders, assumptions, constraints, available authorities, evidence base, and uncertainty.

The system should distinguish descriptive analysis, forecast, scenario, normative judgment, legal interpretation, policy recommendation, and operational decision.

## Source architecture

The policy requires `source_quality_reviewed`. `source_reliability_gap` blocks release when material source reliability, freshness, corroboration, or provenance uncertainty remains unresolved.

`TOOLS/source_registry.py` can preserve source identifier, publisher, date, classification or release status, claim, evidence type, reliability, corroboration, contradiction, confidence, and citation.

## Source hierarchy

Relevant sources can include statutes, treaties, official policy, public strategy documents, budgets, oversight reports, audited data, public intelligence assessments, academic research, technical studies, historical records, reputable journalism, and clearly labeled expert analysis.

Source authority depends on the claim. A policy document may establish official intent but not prove capability performance. A technical study may illuminate a capability but not establish legal authority.

## Freshness

Defense-policy conditions can change quickly. Force structure, budgets, alliances, sanctions, technology, industrial capacity, conflicts, leadership, doctrine, and law can become stale. Date and valid period should remain visible.

## Corroboration

Material claims should be corroborated where feasible, especially when sources may share a common origin. Repetition is not independent confirmation.

## Contradictory evidence

Conflicting evidence should be preserved rather than averaged into artificial certainty. The analysis should identify why sources differ and what evidence would discriminate among interpretations.

## Confidence

Confidence should reflect evidence quality and uncertainty, not rhetorical strength. High confidence requires stronger support than a plausible narrative.

## Assumption discipline

`TOOLS/assumption_log.py` can preserve assumption, rationale, source, sensitivity, owner, status, and consequences if wrong.

Assumptions about adversary intent, allied behavior, technology, timelines, political tolerance, industrial capacity, public support, and escalation should be explicit.

## Alternative hypotheses

The policy can block on `bias_alternative_gap`. Analysts should consider credible alternative explanations and not optimize only for the first coherent narrative.

## Analytic bias

Relevant risks include confirmation bias, mirror imaging, availability bias, anchoring, groupthink, motivated reasoning, survivorship bias, base-rate neglect, and overreliance on vivid recent events.

## Capability context

The policy requires `capability_context_reviewed`. Capability analysis in F147 remains high level and policy oriented.

It can consider mission categories, readiness concepts, resilience, interoperability, sustainment, workforce, training, industrial base, acquisition, technology maturity, logistics at a non-operational level, infrastructure, and strategic dependencies.

## Capability claims

Capability should not be inferred from platform existence alone. Availability, readiness, training, maintenance, sustainment, doctrine, integration, communications, environment, countermeasures, and political constraints can matter.

## Readiness

Readiness is multidimensional and often time sensitive. Publicly available readiness indicators may be incomplete. F147 should not fabricate readiness or operational availability.

## Resilience

Resilience can include redundancy, repair, supply-chain diversity, cyber resilience, infrastructure protection, workforce continuity, communications, and recovery capacity.

## Industrial base

High-level industrial-base analysis can examine production capacity, workforce, suppliers, lead times, materials, manufacturing resilience, procurement incentives, surge concepts, and allied production without providing instructions for weapon construction.

## Acquisition policy

Acquisition analysis can address governance, requirements, competition, testing, cost, schedule, technology risk, interoperability, vendor lock-in, sustainment, accountability, and oversight.

## Emerging technology

Policy analysis can cover AI, autonomy, cyber capabilities, space systems, sensing, communications, quantum technology, biotechnology, advanced manufacturing, and other emerging areas at a strategic and governance level.

## AI and autonomy

AI policy should consider reliability, human control, testing, verification, accountability, data quality, adversarial conditions, automation bias, escalation, explainability, cybersecurity, and meaningful governance.

F147 must not provide operational targeting workflows or autonomous weapon-employment instructions.

## Cyber policy

Cyber-defense policy can address resilience, governance, norms, incident coordination, supply-chain security, workforce, critical infrastructure, alliance cooperation, and strategic risk. It should not provide intrusion, persistence, destructive, or evasion instructions.

## Space policy

Space policy can consider resilience, norms, debris, commercial dependencies, allied coordination, dual-use systems, strategic stability, and governance without operational attack planning.

## Nuclear policy

Nuclear-policy analysis requires exceptional care around deterrence, command and control, escalation, arms control, nonproliferation, safety, security, and humanitarian consequences. F147 does not provide weapon design, employment optimization, targeting, or operational launch guidance.

## Biological and chemical security policy

Analysis can address nonproliferation, preparedness, treaty compliance, biosafety, biosecurity, chemical safety, attribution challenges, public health, and governance. It must not provide synthesis, weaponization, dissemination, or optimization instructions.

## Policy architecture

The policy requires `policy_options_reviewed`. `TOOLS/options_matrix.py` can structure option, objective, authority, benefit, cost, implementation dependency, reversibility, evidence, uncertainty, legal issue, civilian impact, escalation risk, and decision status.

## Policy objectives

Objectives should be explicit enough to evaluate alternatives. Ambiguous objectives can make any preferred option appear successful after the fact.

## Options

A policy package should include meaningful alternatives, including where appropriate maintaining current policy, delaying pending evidence, piloting, narrowing scope, using diplomatic or economic instruments, strengthening resilience, or changing governance rather than assuming a military response is required.

## Tradeoffs

Tradeoffs can involve deterrence, reassurance, alliance cohesion, cost, readiness, industrial capacity, civilian consequences, escalation, legitimacy, reversibility, time, opportunity cost, and long-term strategic effects.

## Reversibility

Reversible options can preserve decision space under uncertainty. Irreversible or escalatory options deserve higher review thresholds.

## Implementation

Policy implementation can depend on legislation, budgets, acquisition, diplomacy, alliances, public communication, workforce, infrastructure, technology, oversight, and time. F147 does not translate policy into tactical or targeting instructions.

## Deterrence

Deterrence analysis should distinguish capability, credibility, communication, perception, interests, resolve, and the possibility of misinterpretation. Deterrence is not mechanically predictable.

## Assurance

Policies intended to deter an adversary can also affect allies and partners. Assurance, burden sharing, interoperability, political cohesion, and regional perceptions should be considered.

## Strategic competition

Competition can involve military, diplomatic, economic, technological, informational, industrial, legal, and institutional dimensions. F147 should avoid framing every interaction as zero sum when cooperative or risk-reduction options exist.

## Alliances and partnerships

Alliance analysis should distinguish formal commitments, political expectations, capabilities, domestic constraints, interoperability, geography, burden sharing, and escalation implications.

## Arms control

Arms-control and confidence-building analysis can include verification, transparency, compliance, incentives, breakout risk, crisis communication, norms, and strategic stability.

## Nonproliferation

Nonproliferation policy can examine treaties, safeguards, export controls, diplomacy, sanctions, verification, security assistance, threat reduction, and institutional capacity at a high level.

## Sanctions and economic instruments

Analysis can consider objectives, targeting at the policy level, humanitarian effects, evasion risk at a non-instructional level, enforcement capacity, allied coordination, substitution, second-order effects, and exit conditions.

F147 does not provide sanctions-evasion methods.

## Security assistance

Security-assistance analysis can examine strategic objectives, governance, end-use monitoring, civilian protection, corruption risk, sustainment, training, human rights, interoperability, escalation, and long-term dependency.

## Defense budgeting

Budget analysis can examine force structure, readiness, personnel, acquisition, R&D, infrastructure, operations, maintenance, industrial-base investments, opportunity costs, and fiscal sustainability.

## Opportunity cost

Resources committed to one mission or capability are unavailable for others. Analysis should preserve opportunity costs rather than presenting each program independently.

## Legal and ethical architecture

The policy requires `legal_ethics_reviewed`. `legal_ethics_gap` blocks release when material domestic-law, international-law, rules, authority, human-rights, or ethical questions remain unresolved.

F147 can identify legal questions and summarize authoritative public sources, but it does not provide binding legal advice or determine lawful authority.

## Domestic authority

Use-of-force authority, appropriations, oversight, procurement, intelligence, emergency powers, export controls, sanctions, and other issues can depend on jurisdiction-specific law and current facts.

## International law

Relevant bodies of law can include the UN Charter, law of armed conflict, international humanitarian law, human rights law, treaty obligations, customary international law, neutrality, arms control, and other applicable frameworks.

## Civilian protection

The policy requires `civilian_harm_reviewed`. `civilian_harm_risk` blocks release when material civilian protection, humanitarian, proportionality, discrimination, or downstream harm concerns remain unresolved.

F147 keeps civilian protection central to policy analysis and does not convert legal principles into targeting instructions.

## Human rights

Defense policy can affect detention, surveillance, displacement, expression, privacy, discrimination, humanitarian access, migration, and other rights. These impacts should be surfaced explicitly.

## Ethics

Ethical review can include human dignity, accountability, responsibility, discrimination, proportionality at a policy level, transparency, intergenerational effects, moral injury, and the consequences of delegating decisions to machines.

## Civilian oversight

Democratic systems can include elected leadership, legislative oversight, courts, inspectors general, auditors, independent review, public reporting, and civil society. F147 should not bypass legitimate oversight.

## Risk architecture

The policy requires `escalation_risk_reviewed`. `escalation_strategic_risk` blocks release when material escalation, misperception, alliance, deterrence, proliferation, crisis-stability, or strategic-risk issues remain unresolved.

`TOOLS/risk_register.py` can preserve risk, cause, consequence, likelihood range, severity, uncertainty, indicators, mitigation, owner, residual risk, and review status.

## Escalation

Escalation can occur through deliberate choice, accident, misperception, unauthorized action, cyber effects, alliance dynamics, domestic politics, or interactions among multiple actors.

## Crisis stability

Policy choices can affect incentives to act quickly in a crisis. Systems perceived as vulnerable, opaque, automated, or dual use can increase instability.

## Misperception

An action intended as reassurance may be interpreted as preparation for attack, and an action intended as deterrence may be read as coercion. Analysis should consider multiple audiences.

## Proliferation risk

Technology transfer, alliance policy, export controls, acquisition, and security assistance can create proliferation and diffusion risks beyond the immediate policy objective.

## Second-order effects

Policies can reshape alliances, markets, domestic politics, industrial capacity, technology diffusion, humanitarian conditions, adversary behavior, and future bargaining positions.

## Tail risks

Low-probability, high-consequence outcomes should not disappear because their expected value is difficult to quantify.

## Uncertainty

Uncertainty should be carried through the analysis. F147 should avoid single-point forecasts when outcomes depend on adversary decisions, political events, technological performance, or escalation dynamics.

## Red teaming

Red teaming can challenge assumptions, identify alternative interpretations, test policy logic, and surface failure modes. It must remain at a strategic policy level and not become operational attack planning.

## Wargaming

F147 may discuss wargaming as a policy-analysis methodology, including assumptions, scenario design, adjudication, bias, learning objectives, and limitations. It does not generate tactical battle plans or targeting solutions.

## Scenario analysis

Scenarios can explore plausible futures, decision points, alliance responses, technology change, economic conditions, escalation pathways, and policy robustness. Scenarios are not predictions.

## Indicators and warnings

High-level indicators can identify what evidence would change a policy judgment. F147 should not provide operational surveillance or targeting instructions.

## Classified and sensitive information

The policy requires `classification_release_reviewed`. `classified_sensitive_gap` blocks release when classification, controlled-information, operational-security, privacy, or release-status issues remain unresolved.

F147 should not solicit classified information. Public repositories should not contain classified, export-controlled, controlled unclassified, operationally sensitive, or unlawfully disclosed material.

## Operational security

Even individually public facts can create risk when aggregated into a current operational picture. F147 should avoid generating detailed current force locations, vulnerabilities, movement patterns, schedules, readiness states, or other information that materially enables harm.

## Privacy

Defense and security analysis can involve personnel, contractors, officials, service members, families, and civilians. Personally identifiable or sensitive personal information should be minimized and protected.

## Actionable-harm boundary

`operationalization_risk` blocks release when analysis would materially enable targeting, weapon construction, evasion, force employment, or other actionable harm.

The boundary applies regardless of whether individual source facts are public.

## Targeting boundary

`select_or_prioritize_target` is protected. F147 does not identify, rank, optimize, or recommend real-world targets for attack.

## Weapon boundary

`authorize_weapon_employment` is protected. The system does not provide weapon construction, modification, employment optimization, firing solutions, vulnerability exploitation, or attack-effect instructions.

## Use-of-force boundary

`authorize_use_of_force` is protected. Policy analysis can discuss authorities and strategic considerations, but only lawful human authorities can decide on force.

## Operational-plan boundary

`approve_operational_plan` is protected. F147 does not produce or approve tactical or operational battle plans.

## Command boundary

`issue_operational_command` and `external_operational_distribution` are protected. The system cannot issue orders or distribute operational instructions.

## Information operations

Policy-level analysis can examine information integrity, strategic communication, foreign influence, resilience, propaganda risks, and governance. F147 should not design deceptive influence campaigns targeting real populations or individuals.

## Disinformation

The system should not manufacture false narratives, forged evidence, fake official communications, or deceptive personas. It can analyze disinformation and resilience strategies.

## Cyber boundary

F147 can analyze cyber strategy, doctrine, resilience, norms, and governance. It should not provide exploit chains, credential theft, malware, destructive actions, persistence, stealth, or operational intrusion instructions.

## Intelligence boundary

The system can analyze public intelligence assessments, analytic methods, uncertainty, oversight, and policy implications. It does not conduct covert collection, identify intelligence targets, or instruct users how to evade detection.

## Surveillance and civil liberties

Security policy can affect privacy, speech, association, due process, discrimination, and oversight. Surveillance proposals should include necessity, proportionality, authority, minimization, retention, access, auditing, and abuse-risk analysis.

## Export controls

Defense technology and technical data can be subject to export controls. F147 does not determine export classification or authorize transfers. Qualified professionals should review applicable requirements.

## Supply-chain security

High-level analysis can consider concentration, foreign dependency, counterfeit risk, cyber compromise, single points of failure, critical materials, trusted suppliers, and resilience.

## Research security

Research security should balance legitimate protection of sensitive technology with scientific openness, nondiscrimination, due process, collaboration, and clear legal requirements.

## Dual-use technology

Dual-use technologies can create both civilian benefit and security risk. Analysis should consider governance, access, safeguards, misuse, diffusion, and proportionality without assuming restriction is always the optimal response.

## Human-machine decision making

Defense AI policy should preserve human responsibility. Automation can support analysis but should not obscure accountability for decisions affecting life, liberty, rights, or use of force.

## Automation bias

Decision makers can overtrust apparently precise model outputs. F147 should expose uncertainty, source quality, assumptions, dissent, and model limitations.

## Model risk

Models can fail under distribution shift, adversarial conditions, sparse data, hidden assumptions, feedback loops, or changing strategic behavior. Evaluation should include failure modes rather than only average accuracy.

## Strategic forecasting

Forecasts should use ranges, scenarios, indicators, and explicit assumptions. Political and conflict forecasting has substantial irreducible uncertainty.

## Cost and feasibility

Policy options should include fiscal cost, implementation time, institutional capacity, legal authority, industrial capacity, workforce, alliance requirements, political feasibility, and opportunity cost.

## Metrics

Metrics should match policy objectives and should not reward easily measured activity over strategic outcomes. Quantitative indicators should be paired with qualitative interpretation where needed.

## Evaluation

Policy evaluation can compare intended outcomes, observed effects, unintended consequences, distributional effects, costs, escalation, alliance impacts, and changing assumptions.

## Reversibility and off-ramps

Analysis should identify conditions for review, modification, suspension, termination, negotiation, de-escalation, and other off-ramps where appropriate.

## Decision records

Policy decision records should preserve question, options, evidence, assumptions, legal issues, civilian impacts, risks, dissent, decision authority, rationale, date, and review conditions.

## Provenance

`provenance_documentation_gap` blocks release when source, assumption, estimate, scenario, option, legal basis, or decision provenance is incomplete.

F147 must never fabricate intelligence, capability data, official positions, legal authority, classified status, casualty estimates, policy approval, treaty obligations, source confidence, or decision-maker endorsement.

## Memory and state

The `memory/` layer can preserve sources, assumptions, policy questions, options, scenarios, risks, legal issues, civilian-protection findings, approvals, dissent, and unresolved questions.

It should distinguish verified source material, analyst judgment, scenario assumptions, model output, legal questions, policy proposals, adopted policy, and superseded versions.

## Observability

The `observability/` layer supports traceability across sources, capability claims, assumptions, options, legal and ethical findings, civilian protection, escalation risk, classification and release status, provenance, approvals, and protected-action attempts.

Useful telemetry includes source age, corroboration state, assumption sensitivity, unresolved alternatives, legal blockers, civilian-harm blockers, escalation risks, classification status, approval state, and attempted operationalization.

## Required reviews

The executable policy requires all eight conditions:

```text
source_quality_reviewed
capability_context_reviewed
policy_options_reviewed
legal_ethics_reviewed
civilian_harm_reviewed
escalation_risk_reviewed
classification_release_reviewed
qualified_policy_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- material source reliability, freshness, corroboration, or provenance uncertainty remains unresolved
- classification, controlled-information, operational-security, privacy, or release-status issues remain unresolved
- analysis would materially enable targeting, weapon construction, evasion, force employment, or other actionable harm
- domestic-law, international-law, authority, human-rights, or ethical questions remain unresolved
- civilian protection, humanitarian, proportionality, discrimination, or downstream harm concerns remain unresolved
- escalation, misperception, alliance, deterrence, proliferation, crisis-stability, or strategic risks remain unresolved
- analytic bias, alternative hypotheses, adversarial assumptions, or uncertainty treatment remain materially incomplete
- source, assumption, estimate, scenario, option, legal-basis, or decision provenance is incomplete
- any required review is missing
- qualified policy approval is missing

The system exposes blockers rather than manufacturing intelligence, certainty, legal authority, policy endorsement, classification status, operational validity, or command approval.

## Protected actions

The safety policy permanently protects:

```text
authorize_use_of_force
approve_operational_plan
select_or_prioritize_target
authorize_weapon_employment
issue_operational_command
external_operational_distribution
```

These remain outside autonomous authority even after all required reviews are satisfied.

## Human authority boundaries

F147 must not autonomously authorize force, approve operational plans, select targets, authorize weapon employment, issue military or security commands, make binding legal determinations, declassify information, commit government resources, establish official policy, or distribute operational instructions.

Lawful civilian authorities, military command, legal counsel, intelligence authorities, oversight bodies, elected officials, and qualified policy professionals retain their respective authority.

## Explicit failure states

```text
SOURCE QUALITY REVIEW REQUIRED
CAPABILITY CONTEXT REVIEW REQUIRED
POLICY OPTIONS REVIEW REQUIRED
LEGAL AND ETHICS REVIEW REQUIRED
CIVILIAN HARM REVIEW REQUIRED
ESCALATION RISK REVIEW REQUIRED
CLASSIFICATION AND RELEASE REVIEW REQUIRED
QUALIFIED POLICY APPROVAL REQUIRED
SOURCE RELIABILITY GAP
CLASSIFIED OR SENSITIVE INFORMATION GAP
OPERATIONALIZATION RISK
LEGAL OR ETHICAL GAP
CIVILIAN HARM RISK
ESCALATION OR STRATEGIC RISK
BIAS OR ALTERNATIVE-HYPOTHESIS GAP
PROVENANCE DOCUMENTATION GAP
USE OF FORCE AUTHORIZATION PROHIBITED
OPERATIONAL PLAN APPROVAL PROHIBITED
TARGET SELECTION PROHIBITED
WEAPON EMPLOYMENT AUTHORIZATION PROHIBITED
OPERATIONAL COMMAND PROHIBITED
EXTERNAL OPERATIONAL DISTRIBUTION PROHIBITED
```

## End-to-end reference workflow

1. Define the policy question, decision context, jurisdiction, horizon, objectives, stakeholders, authorities, constraints, and uncertainty.
2. Register sources with date, provenance, release status, claim, reliability, corroboration, contradiction, and confidence.
3. Record assumptions and identify evidence that would confirm, weaken, or overturn them.
4. Build high-level capability context without operational employment, targeting, vulnerability exploitation, or weapon-construction detail.
5. Develop multiple policy alternatives with objectives, authority, cost, feasibility, reversibility, implementation dependencies, and uncertainty.
6. Review domestic and international legal questions, ethics, human rights, oversight, and civilian-protection implications.
7. Review deterrence, assurance, alliance effects, escalation, misperception, proliferation, crisis stability, second-order effects, and tail risks.
8. Challenge the analysis with alternative hypotheses, red-team questions, scenario variation, and sensitivity analysis at a policy level.
9. Verify classification, release, privacy, operational-security, and aggregation risk before distribution.
10. Preserve provenance for sources, assumptions, estimates, scenarios, options, legal bases, dissent, approvals, and decisions.
11. Apply fail-closed governance and require qualified policy approval.
12. Keep use of force, operational planning, target selection, weapon employment, operational command, and operational distribution outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test source discipline, uncertainty, alternative hypotheses, high-level capability framing, policy-option quality, legal and ethical awareness, civilian protection, escalation analysis, classification discipline, provenance, actionable-harm boundaries, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved high-level support release, source-reliability gaps, classified or sensitive-information gaps, operationalization risk, legal or ethical gaps, civilian-harm risks, escalation or strategic risks, analytic-bias gaps, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed high-level policy workflow.

## Reproducibility

Reproducible defense-policy review requires preserving source versions, dates, citations, assumptions, capability claims, scenario definitions, options, legal questions, civilian-protection findings, strategic risks, classification and release status, dissent, approvals, and unresolved issues.

## Extension points

Organization-specific implementations can add governed integrations for public policy libraries, legislation, treaty databases, budget data, oversight reports, acquisition systems, public strategy documents, approved internal knowledge systems, scenario tools, and decision-record systems.

Any integration capable of accessing controlled information, changing official policy, issuing commands, committing resources, transmitting operational information, or affecting real-world force decisions should remain behind appropriate authorization, least privilege, access controls, audit logging, classification controls, and human-controlled execution.

## Example applications

Potential governed uses include defense-strategy research, capability-policy review, acquisition-policy analysis, alliance-policy analysis, resilience planning, industrial-base policy, emerging-technology governance, AI and autonomy policy, arms-control analysis, nonproliferation policy, security-assistance review, defense-budget analysis, civilian-protection policy, oversight support, strategic-risk analysis, and academic strategic studies.

F147 is not an autonomous commander, targeter, weapon designer, weapons-employment advisor, intelligence collection system, covert operator, legal authority, declassification authority, policy maker, or use-of-force decision maker.

## Design principles

1. Begin with a clearly bounded policy question, lawful authority, traceable sources, and explicit uncertainty.
2. Separate evidence, assumptions, estimates, scenarios, legal questions, normative judgments, and recommendations.
3. Preserve alternative hypotheses and dissent rather than forcing consensus.
4. Keep capability analysis high level and do not operationalize it into targeting, weapon employment, or actionable harm.
5. Center civilian protection, human rights, legal constraints, oversight, escalation, and strategic stability.
6. Never fabricate intelligence, capability facts, official positions, legal authority, classification status, or approvals.
7. Protect sensitive information and consider aggregation risk even when individual facts are public.
8. Fail closed when evidence, classification, operationalization, law, ethics, civilian harm, escalation, analytic alternatives, provenance, or approval is incomplete.
9. Keep force, targeting, weapons, operations, command, declassification, and binding policy authority under lawful human control.

## Scope statement

F147 demonstrates a governed multi-agent architecture for high-level defense-policy analysis. It combines specialized source, capability, policy, legal-and-ethics, and risk agents with deterministic source, assumption, options, risk, and review tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over force, operations, targeting, weapon employment, command, controlled information, and binding policy decisions.

Author: Mahsa Keikha
