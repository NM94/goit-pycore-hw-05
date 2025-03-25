from typing import Callable,Generator
import re


def generator_numbers(text: str) -> Generator[float,None,None]:
    numbers = re.findall(r"\d+\.\d+", text) 
    for num in numbers: 
        yield float(num)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float: 
       return sum(func(text))



