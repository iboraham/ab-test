def _check_test_type(tt: str):
    if tt == "two-tailed" or tt == "left-tailed" or tt == "right-tailed":
        pass
    else:
        raise AttributeError(
            "Test type should be whether 'two-tailed' or 'left-tailed' or 'right-tailed'"
        )


def _check_others(*args):
    for cl in args:
        if cl < 1.0 and cl > 0.0:
            continue
        else:
            raise AttributeError(
                "Confidence level, beta level, before effect and after effect size should be between 1 and 0"
            )


def _check_inputs(test_type, confidence_level, power, before_eff, after_eff):
    _check_test_type(test_type)
    _check_others(confidence_level, power, before_eff, after_eff)
