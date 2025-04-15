from collections.abc import Callable

import streamlit as st


def rot(base: int, offset: int) -> Callable[[str], str]:
    amount = offset * 2

    return lambda s: "".join(
        chr(base + (ord(ch) - base + offset) % amount)
        if ord(ch) in range(base, base + amount)
        else ch
        for ch in s
    )


rot10451 = rot(0x4E00, 10451)
rot13_upper = rot(ord("A"), 13)
rot13_lower = rot(ord("a"), 13)

source = st.text_area(
    "source string",
    help="type any text here, enter to encrypt",
)

result = rot13_upper(rot13_lower(rot10451(source)))

st.text(result)
