from .utils import *
from .utils import _check_inputs
from .h_test import *
import pandas as pd
from math import ceil
import statsmodels.stats.api as sms
from statsmodels.stats.proportion import proportions_ztest, proportion_confint


class Experiment:
    def __init__(self, data):
        self.data = data
        if data.shape[1] == 3:
            self.data.columns = ["user", "group", "converted"]
        elif data.shape[1] == 4:
            self.data.columns = ["user", "group", "landing_page", "converted"]
        elif data.shape[1] == 5:
            self.data.columns = [
                "user",
                "timestamp",
                "group",
                "landing_page",
                "converted",
            ]
        else:
            raise AttributeError("Experiment data should be like in the docs")

    def _design_experiment(self, *args):
        test_type, confidence_level, power, before_eff, after_eff = args

        self.test_type = test_type
        self.confidence_level = confidence_level
        self.alpha = 1 - confidence_level
        self.beta = power
        self.effect_size = sms.proportion_effectsize(before_eff, after_eff)

    def _power_analysis(self):
        n_required = sms.NormalIndPower().solve_power(
            self.effect_size, power=self.beta, alpha=self.alpha, ratio=1
        )
        n_required = ceil(n_required)
        self.n_required = n_required

    def _prepare_data(self):
        df = self.data.copy()
        df.drop_duplicates(subset=["user"], inplace=True)
        self.data = df.copy()

    def _sampling(self):
        df = self.data.copy()
        control_sample = df[df["group"] == "control"].sample(
            n=self.n_required, random_state=42
        )
        treatment_sample = df[df["group"] == "treatment"].sample(
            n=self.n_required, random_state=42
        )

        ab_test_data = pd.concat([control_sample, treatment_sample], axis=0)
        ab_test_data.reset_index(drop=True, inplace=True)
        self.ab_test_data = ab_test_data

    def _collect_and_prepare_data(self):
        self._prepare_data()
        self._sampling()

    def _hypothesis_test(self):
        control_results = self.ab_test_data[self.ab_test_data["group"] == "control"][
            "converted"
        ]
        treatment_results = self.ab_test_data[
            self.ab_test_data["group"] == "treatment"
        ]["converted"]
        n_con = control_results.count()
        n_treat = treatment_results.count()
        successes = [control_results.sum(), treatment_results.sum()]
        nobs = [n_con, n_treat]

        z_stat, pval = proportions_ztest(successes, nobs=nobs)
        (lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(
            successes, nobs=nobs, alpha=0.05
        )
        self.lower_con = lower_con
        self.upper_con = upper_con
        self.lower_treat = lower_treat
        self.upper_treat = upper_treat
        self.z_stat = z_stat
        self.pval = pval

    def fit(self, test_type: str, confidence_level, power, before_eff, after_eff):
        _check_inputs(test_type, confidence_level, power, before_eff, after_eff)
        self._design_experiment(
            test_type, confidence_level, power, before_eff, after_eff
        )
        self._power_analysis()
        self._collect_and_prepare_data()
        self._hypothesis_test()
