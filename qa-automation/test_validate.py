import copy
import unittest
from validate import validate_response, TOOLS

class ResponseValidation(unittest.TestCase):
    def setUp(self):
        self.data = {"brief": "A sourced solution brief. " * 10, "requirements": {"use_case": "retail"},
                     "hardware_options": [{"sku": "example"}], "platform_capabilities": [{"name": "OpenShift"}],
                     "architecture": {"name": "edge"}, "inference_log": [
                         {"node": n, "model": "assigned", "latency_ms": 10}
                         for n in ("understand_requirements", "generate_brief")
                     ] + [{"node": t, "tool": t, "latency_ms": 1} for t in TOOLS]}
    def test_non_object_response_is_rejected(self):
        for data in (None, [], "fallback"):
            with self.assertRaises(ValueError): validate_response(data, "assigned")
    def test_complete_evidence(self):
        self.assertTrue(validate_response(self.data, "assigned"))
    def test_fallback_brief_with_failed_model_is_rejected(self):
        self.data["inference_log"][0]["error"] = "backend failed"
        with self.assertRaises(ValueError): validate_response(self.data, "assigned")
    def test_missing_tools_is_rejected(self):
        self.data["inference_log"] = self.data["inference_log"][:2]
        with self.assertRaises(ValueError): validate_response(self.data, "assigned")
    def test_wrong_model_is_rejected(self):
        with self.assertRaises(ValueError): validate_response(self.data, "wrong")
    def test_empty_structured_results_are_rejected(self):
        self.data["hardware_options"] = []
        with self.assertRaises(ValueError): validate_response(self.data, "assigned")
    def test_invalid_latency_is_rejected(self):
        for latency in (-1, True, None, float("nan"), float("inf")):
            data = copy.deepcopy(self.data)
            data["inference_log"][0]["latency_ms"] = latency
            with self.assertRaises(ValueError): validate_response(data, "assigned")

if __name__ == "__main__": unittest.main()
