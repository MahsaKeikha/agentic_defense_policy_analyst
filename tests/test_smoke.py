from orchestration.orchestrator import run
def test_run(): assert run({'question':'x'})['system']=='F147'
