"""Set up the addition block config"""

from quaisr import Block
from quaisr.types import QuaisrComplexType
from .add import add

if __name__ == "__main__":
    addition_block = Block()
    # Each input is some kind of numeric
    num_type = addition_block.declare_generic("T", upper_bound=QuaisrComplexType())

    # Declare the inputs and outputs
    addition_block.add_input("lhs", num_type).add_input("rhs", num_type).add_output(
        "sum", num_type
    ).set_entrypoint(add).start()
