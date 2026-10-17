# Enterprise AI Workflow Agent

Independent portfolio project: a customer-request workflow with controlled actions and measurable evaluation.

## Current status

In development. The repository currently contains a deterministic local starter, synthetic examples, and an implementation roadmap. LLM integration, authentication, cloud deployment, and benchmark evaluation are planned; no production deployment or performance results are claimed.

## Run the starter

Python 3.10 or newer; no third-party dependencies, API credentials, or network access required.

```sh
python3 demo.py
```

## Implementation roadmap

- [ ] Define source retrieval and unsupported-request behavior.
- [ ] Add a bounded model adapter and structured output validation.
- [ ] Implement explicit authorization, approval, replay and failure controls.
- [ ] Freeze 50 held-out synthetic cases and report actual results.
- [ ] Deploy an authenticated GCP service and document operations.

## Data and responsible use

All examples are synthetic. Do not commit client data, PHI, credentials, or sensitive logs. This is an independent portfolio project, not a customer deployment or a formal compliance assessment.

## Contribution and evidence

Initial scaffolding was created with AI coding assistance under Tony Wang's direction. Future case studies will identify personal contributions, evaluation methods, limitations, and actual measured results. The starter demonstrates only the functionality described above.
