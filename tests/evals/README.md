# Evaluate agent behavior

Package validation checks manifests, references, and boundaries. These scenarios check whether an agent can use the instructions to complete a task and make claims supported by the artifact. They are not a claim of professional quality across every creative task or client.

## Run a scenario

1. Copy the current `skills/` into an isolated directory and record a content hash or source revision. For a before/after comparison, preserve the original skill snapshot first.
2. Select a case in [scenarios.json](scenarios.json). Give a fresh task agent only that case's request, skill location, relevant raw artifact, available tool paths, and the four skills' names/descriptions as a discovery catalog. Do not preload all skill bodies. Run independent cases in separate contexts when measuring skill selection. Keep evaluator acceptance criteria out of the actor's prompt.
3. For a live case, use a temporary project. Keep account access, uploads, publishing, and original user projects outside the test. The actor should perform the task, not describe what it would do.
4. For a decision probe, supply the stated capability/evidence constraints and collect proposed actions. Do not pretend that Editor tools, source files, or captures were actually exercised.
5. Inspect the actual edits, command results, images, landed data, and source preservation. Evaluate against each acceptance criterion, marking pass, fail, or not exercised. A correct recitation does not count as live behavior.
6. Record the tool version, skills/references loaded, evidence, deviations, and material gaps. Re-run only scenarios affected by a subsequent correction.

Use an independent agent when available and authorized. Otherwise run the scenario manually and label that limitation. Live agent sessions consume model resources and can take several minutes; they are not run in ordinary package CI.

## Repair fixture

The helper copies three files from the installed CLI's `rml_vm_input` sample and introduces one broken attachment name. It refuses an existing output directory and leaves the installed sample untouched. This avoids distributing a stale copy of Rive's sample or relying on a contributor-specific path.

```sh
python tests/evals/prepare_fixture.py --rive <installed-executable> --output <new-temporary-directory>
```

The fixture was exercised with CLI 1.3.0. If that sample changes, the helper stops; inspect and adapt the scenario explicitly rather than silently testing a different defect.

## Scope of proof

- `script-input-repair` exercises reproduction, a narrow source fix, data injection, runtime behavior, and headless visual review.
- `new-creative-work` exercises the brief-to-artifact flow and real repeated interaction. A visual reviewer must assess the rendered composition; compilation is insufficient.
- `recoverable-source-copy` checks byte-preserving recovery without adding duplicate compiler inputs, followed by an actual local compilation.
- The remaining cases are decision probes for scope, source preservation, tool boundaries, and honest claims. They do not certify live Editor integration, recovery after a real push/pull, signing, or every runtime.

The evaluation structure takes inspiration from the process skills and behavior testing in [obra/superpowers](https://github.com/obra/superpowers/tree/8ca22dba9a94f28898bbce59f2537ff4d87c747d). IEE's cases and instructions are specific to Rive. The local comparison checkout belongs in ignored `.refrence/`, outside the plugin's validated content.

## Evidence needed for broader readiness claims

Keep a capability unverified until a relevant artifact and interaction have been exercised. A new scenario listed in JSON is planned coverage, not a passing test.

- Discovery: test ordinary requests, narrow edits, and unrelated requests in each client claimed to work automatically. Manually selecting a skill only tests explicit invocation.
- Creative work: cover the kinds of work actually claimed, including supplied-reference fidelity, typography/content variation, expressive motion, and original composition. Separate brief compliance, craft, and handoff judgments; retain images and timing evidence.
- Technical work: exercise supported layouts, data, scripting lanes, shaders, and rigs with meaningful failures or edge cases. One Luau attachment repair does not validate every scripting API.
- Interaction: test promised hit/focus regions, representative boundaries, outside/disabled cases, repetition, and interruption. An empty problem list and one center click are insufficient.
- Editor and delivery: use a real document, preserve source, verify actual edits, and open the produced output in its requested destination. A discovered tool list or successful handshake does not prove authoring or export.
- Repeatability: rerun representative cases with independent sessions and the client/model combinations being claimed. Report failures and recovery cost alongside successes. Do not infer reliability across all agents from one model's trials.

CI currently checks packaging and validator regressions. It does not certify artistic quality, live Editor behavior, or runtime compatibility. Human creative review and destination testing remain separate evidence.
