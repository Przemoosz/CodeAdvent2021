from Day_10_Challange_1 import check_if_corrupted, corrupted_func


class TestOldFunctions:
    """Tests for first prototype search function. Not used in main file"""

    def test_func_if_closed_simple(self) -> None:
        """Func should return True if all parenthesis are closed.
        Testing only one parenthesis type"""
        assert check_if_corrupted("((()))")
        assert check_if_corrupted("<>")
        assert check_if_corrupted("{{}}")
        assert check_if_corrupted("[[[[[]]]]]")

    def test_func_if_closed_mixed_chars(self) -> None:
        """Func should return True if all parenthesis are closed.
        Testing mixed parenthesis type"""
        assert check_if_corrupted("({[]})")
        assert check_if_corrupted("[][][][][]")
        assert check_if_corrupted("[][<>][<<>>]{[]}")


class TestNewFunction:
    """Tests for new correctly working function"""

    def test_simple_func_not_corrupted(self) -> None:
        """Func should return Fine if there is no problem with closing parenthesis"""
        assert corrupted_func("()") == "Fine"
        assert corrupted_func("[]") == "Fine"
        assert corrupted_func("{}") == "Fine"
        assert corrupted_func("<>") == "Fine"
        assert corrupted_func("<((((()))))>") == "Fine"
        assert corrupted_func("<((((({<[{}{}]<<>>()>})))))>") == "Fine"
        assert corrupted_func('[({(<(())[]>[[{[]{<()<>>') == "Fine"

    def test_simple_func_corrupted(self) -> None:
        """Function should return expected closing"""
        assert corrupted_func("(]") == "]"
        assert corrupted_func("([][][<{()()()}>]]") == "]"
        assert corrupted_func("{)") == ")"
        assert corrupted_func("{[][][<{()()()}>]]") == "]"
        assert corrupted_func("<]") == "]"
        assert corrupted_func("<[][][<{()()()}>]]") == "]"
        assert corrupted_func("[>") == ">"
        assert corrupted_func("[{}[]<>>") == ">"

    def test_func_complex_corrupted(self) -> None:
        """Function should also work for larger examples and return expected closing"""
        assert corrupted_func('{([(<{}[<>[]}>{[]{[(<()>') == "}"
        assert corrupted_func('[[<[([]))<([[{}[[()]]]') == ")"
        assert corrupted_func("[{[{({}]{}}([{[{{{}}([]") == "]"
        assert corrupted_func("[<(<(<(<{}))><([]([]()") == ")"
        assert corrupted_func("<{([([[(<>()){}]>(<<{{") == ">"
