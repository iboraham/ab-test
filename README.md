<h1 align="center">Welcome to ab-test 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/iboraham/ab-test/blob/master/README.md" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://pepy.tech/project/ab-test"><img src="https://pepy.tech/badge/ab-test" alt="Downloads"></a>
  <img src='https://bettercodehub.com/edge/badge/iboraham/ab-test?branch=master'>
  <a href="https://opensource.org/licenses/MIT" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://lgtm.com/projects/g/iboraham/ab-test/alerts/"><img alt="Total alerts" src="https://img.shields.io/lgtm/alerts/g/iboraham/ab-test.svg?logo=lgtm&logoWidth=18"/></a>
  <a href="https://lgtm.com/projects/g/iboraham/ab-test/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/iboraham/ab-test.svg?logo=lgtm&logoWidth=18"/></a>
  <a href="https://colab.research.google.com/github/iboraham/ab-test/blob/master/notebooks/example.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
  <a href="https://twitter.com/iboraham" target="_blank">
    <img alt="Twitter: iboraham" src="https://img.shields.io/twitter/follow/iboraham.svg?style=social" />
  </a>
</p>

> A/B testing framework for python

### 🏠 [Homepage](https://github.com/iboraham/ab-test)

## Install

```sh
>> pip install ab-test
```

## Usage

```python
>> import abtest

>> experiment = abtest.Experiment(data)
>> experiment.fit("two-tailed", confidence_level=0.95, power=.8, before_eff=0.09, after_eff=0.12)

"""
z statistic: -2.68
p-value: 0.007
ci 95% for control group: [0.086, 0.116]
ci 95% for treatment group: [0.115, 0.148]
"""
```

## Author

👤 **I.Onur Serbetci**

- Website: www.iboraham.github.io
- Twitter: [@iboraham](https://twitter.com/iboraham)
- Github: [@iboraham](https://github.com/iboraham)
- LinkedIn: [@ionur-serbetci](https://linkedin.com/in/ionur-serbetci)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/iboraham/ab-test/issues).

## Show your support

Give a ⭐️ if this project helped you!

<a href="https://www.patreon.com/iboraham">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## 📝 License

Copyright © 2021 [I.Onur Serbetci](https://github.com/iboraham).<br />
This project is [MIT](https://opensource.org/licenses/MIT) licensed.

---

_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
