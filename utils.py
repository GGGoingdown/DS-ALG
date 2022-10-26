from typing import Any


class ResultValidator:
    def __init__(self, inputs: Any, expected_result: Any) -> None:
        self.inputs = inputs
        self.expected_result = expected_result

    def validate(self, outputs: Any) -> None:
        assert (
            outputs == self.expected_result
        ), f"Inputs: {self.inputs}::Expect: {self.expected_result}::Get: {outputs}"

    def __str__(self) -> str:
        return f"TestCase: {self.inputs}::Expected Result: {self.expected_result}"
