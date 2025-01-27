## 6.11.0 / 2020-03-09

* [Added] Added support to map user defined `stackstate-environment` tags or config to the `environments` object
* [Added] Added support to map user defined `stackstate-layer` tags or config to the `layer` object
* [Added] Added support to map user defined `stackstate-domain` tags or config to the `domain` object
* [Added] Added support to map user defined `stackstate-identifiers` tags or config to the `identifiers` array

## Apply patches up to 6.10.1 / 2019-07-09

## 6.0.1 / 2019-02-20

* [Fixed] Import kubernetes lazily to reduce memory footprint. See [#3166](https://github.com/DataDog/integrations-core/pull/3166).

## 6.0.0 / 2019-02-12

* [Added] Expose the single check instance as an attribute. See [#3093](https://github.com/DataDog/integrations-core/pull/3093).
* [Added] Parse raw yaml instances and init_config with dedicated base class method. See [#3098](https://github.com/DataDog/integrations-core/pull/3098).
* [Added] Add datadog-checks-downloader. See [#3026](https://github.com/DataDog/integrations-core/pull/3026).
* [Fixed] Resolve flake8 issues. See [#3060](https://github.com/DataDog/integrations-core/pull/3060).
* [Fixed] Properly prevent critical logs during testing. See [#3053](https://github.com/DataDog/integrations-core/pull/3053).
* [Changed] Fix riakcs dependencies. See [#3033](https://github.com/DataDog/integrations-core/pull/3033).
* [Added] Support Python 3 Base WMI. See [#3036](https://github.com/DataDog/integrations-core/pull/3036).
* [Added] Upgrade psutil. See [#3019](https://github.com/DataDog/integrations-core/pull/3019).
* [Fixed] Remove extra log about error encoding tag. See [#2976](https://github.com/DataDog/integrations-core/pull/2976).
* [Added] Support Python 3. See [#2835](https://github.com/DataDog/integrations-core/pull/2835).
* [Fixed] Improve log messages for when tags aren't utf-8. See [#2966](https://github.com/DataDog/integrations-core/pull/2966).

## 5.2.0 / 2019-01-16

* [Added] Make service check statuses available as constants. See [#2960][1].

## 5.1.0 / 2019-01-15

* [Fixed] Always ensure_unicode for subprocess output. See [#2941][2].
* [Added] Add round method to checks base. See [#2931][3].
* [Added] Added lxml dependency. See [#2846][4].
* [Fixed] Include count as an aggregate type in tests. See [#2920][5].
* [Added] Support unicode for Python 3 bindings. See [#2869][6].

## 5.0.1 / 2019-01-07

* [Fixed] Fix context limit logic for OpenMetrics checks. See [#2877][7].

## 5.0.0 / 2019-01-04

* [Added] Add kube_controller_manager integration. See [#2845][8].
* [Added] Add kube_leader mixin to monitor leader elections. See [#2796][9].
* [Fixed] Use 'format()' function to create device tag. See [#2822][10].
* [Added] Prevent caching of PDH counter instances by default. See [#2654][11].
* [Added] Prevent critical logs during testing. See [#2840][12].
* [Added] Support trace logging. See [#2838][13].
* [Fixed] Bump pyodbc for python3.7 compatibility. See [#2801][14].
* [Added] Bump psycopg2-binary version to 2.7.5. See [#2799][15].
* [Fixed] Fix metric normalization function for Python 3. See [#2784][16].
* [Added] Support Python 3. See [#2780][17].
* [Changed] Bump kafka-python and kazoo. See [#2766][18].
* [Added] Support Python 3. See [#2738][19].

## 4.6.0 / 2018-12-07

* [Added] Fix unicode handling of log messages. See [#2698][20].
* [Fixed] Ensure unicode for subprocess output. See [#2697][21].

## 4.5.0 / 2018-12-02

* [Added] Improve OpenMetrics label joins. See [#2624][22].

## 4.4.0 / 2018-11-30

* [Added] Add linux as supported OS. See [#2614][23].
* [Added] Upgrade cryptography. See [#2659][24].
* [Added] Upgrade requests. See [#2656][25].
* [Fixed] Fix not_asserted aggregator stub function. See [#2639][26].
* [Added] Log line where `AgentCheck.warning` was called in the check. See [#2620][27].
* [Fixed] Fix requirements-agent-release.txt updating. See [#2617][28].

## 4.3.0 / 2018-11-12

* [Added] Add option to prevent subprocess command logging. See [#2565][29].
* [Added] Support Kerberos auth. See [#2516][30].
* [Added] Add option to send additional metric tags for Open Metrics. See [#2514][31].
* [Added] Add standard ssl_verify option to Open Metrics. See [#2507][32].
* [Added] Winpdh improve exception messages. See [#2486][33].
* [Added] Upgrade requests. See [#2481][34].
* [Fixed] Fix bug making the network check read /proc instead of /host/proc on containers. See [#2460][35].
* [Added] Fix unicode handling on A6. See [#2435][36].

##### Rename to stackstate_checks_base

# CHANGELOG - datadog_checks_base

## 4.2.0 / 2018-10-16

* [Added] Expose text conversion methods. See [#2420](https://github.com/DataDog/integrations-core/pull/2420).
* [Fixed] Handle unicode strings in non-float handler's error message. See [#2419](https://github.com/DataDog/integrations-core/pull/2419).

## 4.1.0 / 2018-10-12

* [Added] Expose core functionality at the root. See [#2394](https://github.com/DataDog/integrations-core/pull/2394).
* [Added] base: add check name to Limiter warning message. See [#2391](https://github.com/DataDog/integrations-core/pull/2391).
* [Fixed] Fix import of _get_py_loglevel. See [#2383](https://github.com/DataDog/integrations-core/pull/2383).
* [Fixed] Fix hostname override and type for status_report.count metrics. See [#2372](https://github.com/DataDog/integrations-core/pull/2372).

## 4.0.0 / 2018-10-11

* [Added] Added generic error class ConfigurationError. See [#2367](https://github.com/DataDog/integrations-core/pull/2367).
* [Changed] Add base subpackage to datadog_checks_base. See [#2331](https://github.com/DataDog/integrations-core/pull/2331).
* [Added] Freeze Agent requirements. See [#2328](https://github.com/DataDog/integrations-core/pull/2328).
* [Added] Pin pywin32 dependency. See [#2322](https://github.com/DataDog/integrations-core/pull/2322).

## 3.0.0 / 2018-09-25

* [Added] Adds ability to Trace "check" function with DD APM. See [#2079](https://github.com/DataDog/integrations-core/pull/2079).
* [Changed] Catch exception when string sent as metric value. See [#2293](https://github.com/DataDog/integrations-core/pull/2293).
* [Changed] Revert default prometheus metric limit to 2000. See [#2248](https://github.com/DataDog/integrations-core/pull/2248).
* [Fixed] Fix base class imports for Agent 5. See [#2232](https://github.com/DataDog/integrations-core/pull/2232).

## 2.2.1 / 2018-09-11

* [Fixed] Temporarily increase the limit of prometheus metrics sent for 6.5. See [#2214](https://github.com/DataDog/integrations-core/pull/2214).

## 2.2.0 / 2018-09-06

* [Changed] Freeze pyVmomi dep in base check. See [#2181](https://github.com/DataDog/integrations-core/pull/2181).

## 2.1.0 / 2018-09-05

* [Changed] Change order of precedence of whitelist and blacklist for pattern filtering. See [#2174](https://github.com/DataDog/integrations-core/pull/2174).

## 2.0.0 / 2018-09-04

* [Added] Add cluster-name suffix to node-names in kubernetes state. See [#2069](https://github.com/DataDog/integrations-core/pull/2069).
* [Added] Limit Prometheus/OpenMetrics checks to 2000 metrics per run by default. See [#2093](https://github.com/DataDog/integrations-core/pull/2093).
* [Changed] Allow checks to manually specify in their configuration which defaults to use. See [#2145](https://github.com/DataDog/integrations-core/pull/2145).
* [Fixed] Moves WMI Check to Pytest. See [#2133](https://github.com/DataDog/integrations-core/pull/2133).
* [Changed] Use different defaults if scraper_config is created by OpenMetricsBaseCheck. See [#2135](https://github.com/DataDog/integrations-core/pull/2135).
* [Fixed] Fix Prometheus scraping for Python 3. See [#2128](https://github.com/DataDog/integrations-core/pull/2128).
* [Changed] Drop protobuf support for OpenMetrics. See [#2098](https://github.com/DataDog/integrations-core/pull/2098).
* [Added] Add code coverage. See [#2105](https://github.com/DataDog/integrations-core/pull/2105).
* [Changed] Create OpenMetricsBaseCheck, an improved version of GenericPrometheusCheck. See [#1976](https://github.com/DataDog/integrations-core/pull/1976).
* [Fixed] Move RiakCS to pytest, fixes duped tags in RiakCS, adds google_cloud_engine pip dep. See [#2081](https://github.com/DataDog/integrations-core/pull/2081).

## 1.5.0 / 2018-08-19

* [Added] Allow installation of base dependencies. See [#2067](https://github.com/DataDog/integrations-core/pull/2067).
* [Fixed] Retrieve no_proxy directly from the Datadog Agent's configuration. See [#2004](https://github.com/DataDog/integrations-core/pull/2004).
* [Added] Support Python 3 for datadog_checks_base. See [#1957](https://github.com/DataDog/integrations-core/pull/1957).
* [Fixed] Properly skip proxy environment variables. See [#1935](https://github.com/DataDog/integrations-core/pull/1935).
* [Fixed] Update cryptography to 2.3. See [#1927](https://github.com/DataDog/integrations-core/pull/1927).

## 1.4.0 / 2018-07-18

* [Fixed] fix packaging of agent requirements. See [#1911](https://github.com/DataDog/integrations-core/pull/1911).
* [Fixed] Properly use skip_proxy for instance configuration. See [#1880](https://github.com/DataDog/integrations-core/pull/1880).
* [Fixed] Sync WMI utils from dd-agent to datadog-checks-base. See [#1897](https://github.com/DataDog/integrations-core/pull/1897).
* [Fixed] Improve check performance by filtering it's input before parsing. See [#1875](https://github.com/DataDog/integrations-core/pull/1875).
* [Changed] Bump prometheus client library to 0.3.0. See [#1866](https://github.com/DataDog/integrations-core/pull/1866).
* [Added] Make HTTP request timeout configurable in prometheus checks. See [#1790](https://github.com/DataDog/integrations-core/pull/1790).

## 1.3.2 / 2018-06-15

* [Changed] Bump requests to 2.19.1. See [#1743](https://github.com/DataDog/integrations-core/pull/1743).

## 1.3.1 / 2018-06-13

* [Fixed] upgrade requests dependency. See [#1734](https://github.com/DataDog/integrations-core/pull/1734).
* [Changed] Set requests stream option to false when scraping Prometheus endpoints. See [#1596](https://github.com/DataDog/integrations-core/pull/1596).

## 1.3.0 / 2018-06-07

* [Fixed] change default value of AgentCheck.check_id for Agent 6. See [#1652](https://github.com/DataDog/integrations-core/pull/1652).
* [Added] Support for gathering metrics from prometheus endpoint for the kubelet itself.. See [#1581](https://github.com/DataDog/integrations-core/pull/1581).
* [Added] include wmi for compat. See [#1565](https://github.com/DataDog/integrations-core/pull/1565).
* [Added] added missing tailfile util. See [#1566](https://github.com/DataDog/integrations-core/pull/1566).
* [Fixed] [base] when running A6, mirror logging behavior. See [#1561](https://github.com/DataDog/integrations-core/pull/1561).

## 1.2.2 / 2018-05-11

* [FEATURE] The generic Prometheus check will now send counter as monotonic counter.
* [BUG] Prometheus requests can use an insecure option
* [BUG] Correctly handle missing counters/strings in PDH checks when possible
* [BUG] Fix Prometheus Scrapper logger
* [SANITY] Clean-up export for `PDHBaseCheck` + export `WinPDHCounter`. [#1183][83]
* [IMPROVEMENT] Discard metrics with invalid values

## 1.2.1 / 2018-03-23

* [BUG] Correctly handle internationalized versions of Windows in the PDH library.
* [FEATURE] Keep track of Service Checks in the Aggregator stub.

## 1.1.0 / 2018-03-23

* [FEATURE] Add a generic prometheus check base class & rework prometheus check using a mixin

## 1.0.0 / 2017-03-22

* [FEATURE] adds `datadog_checks`

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2960
[2]: https://github.com/DataDog/integrations-core/pull/2941
[3]: https://github.com/DataDog/integrations-core/pull/2931
[4]: https://github.com/DataDog/integrations-core/pull/2846
[5]: https://github.com/DataDog/integrations-core/pull/2920
[6]: https://github.com/DataDog/integrations-core/pull/2869
[7]: https://github.com/DataDog/integrations-core/pull/2877
[8]: https://github.com/DataDog/integrations-core/pull/2845
[9]: https://github.com/DataDog/integrations-core/pull/2796
[10]: https://github.com/DataDog/integrations-core/pull/2822
[11]: https://github.com/DataDog/integrations-core/pull/2654
[12]: https://github.com/DataDog/integrations-core/pull/2840
[13]: https://github.com/DataDog/integrations-core/pull/2838
[14]: https://github.com/DataDog/integrations-core/pull/2801
[15]: https://github.com/DataDog/integrations-core/pull/2799
[16]: https://github.com/DataDog/integrations-core/pull/2784
[17]: https://github.com/DataDog/integrations-core/pull/2780
[18]: https://github.com/DataDog/integrations-core/pull/2766
[19]: https://github.com/DataDog/integrations-core/pull/2738
[20]: https://github.com/DataDog/integrations-core/pull/2698
[21]: https://github.com/DataDog/integrations-core/pull/2697
[22]: https://github.com/DataDog/integrations-core/pull/2624
[23]: https://github.com/DataDog/integrations-core/pull/2614
[24]: https://github.com/DataDog/integrations-core/pull/2659
[25]: https://github.com/DataDog/integrations-core/pull/2656
[26]: https://github.com/DataDog/integrations-core/pull/2639
[27]: https://github.com/DataDog/integrations-core/pull/2620
[28]: https://github.com/DataDog/integrations-core/pull/2617
[29]: https://github.com/DataDog/integrations-core/pull/2565
[30]: https://github.com/DataDog/integrations-core/pull/2516
[31]: https://github.com/DataDog/integrations-core/pull/2514
[32]: https://github.com/DataDog/integrations-core/pull/2507
[33]: https://github.com/DataDog/integrations-core/pull/2486
[34]: https://github.com/DataDog/integrations-core/pull/2481
[35]: https://github.com/DataDog/integrations-core/pull/2460
[36]: https://github.com/DataDog/integrations-core/pull/2435
[37]: https://github.com/DataDog/integrations-core/pull/2420
[38]: https://github.com/DataDog/integrations-core/pull/2419
[39]: https://github.com/DataDog/integrations-core/pull/2394
[40]: https://github.com/DataDog/integrations-core/pull/2391
[41]: https://github.com/DataDog/integrations-core/pull/2383
[42]: https://github.com/DataDog/integrations-core/pull/2372
[43]: https://github.com/DataDog/integrations-core/pull/2367
[44]: https://github.com/DataDog/integrations-core/pull/2331
[45]: https://github.com/DataDog/integrations-core/pull/2328
[46]: https://github.com/DataDog/integrations-core/pull/2322
[47]: https://github.com/DataDog/integrations-core/pull/2079
[48]: https://github.com/DataDog/integrations-core/pull/2293
[49]: https://github.com/DataDog/integrations-core/pull/2248
[50]: https://github.com/DataDog/integrations-core/pull/2232
[51]: https://github.com/DataDog/integrations-core/pull/2214
[52]: https://github.com/DataDog/integrations-core/pull/2181
[53]: https://github.com/DataDog/integrations-core/pull/2174
[54]: https://github.com/DataDog/integrations-core/pull/2069
[55]: https://github.com/DataDog/integrations-core/pull/2093
[56]: https://github.com/DataDog/integrations-core/pull/2145
[57]: https://github.com/DataDog/integrations-core/pull/2133
[58]: https://github.com/DataDog/integrations-core/pull/2135
[59]: https://github.com/DataDog/integrations-core/pull/2128
[60]: https://github.com/DataDog/integrations-core/pull/2098
[61]: https://github.com/DataDog/integrations-core/pull/2105
[62]: https://github.com/DataDog/integrations-core/pull/1976
[63]: https://github.com/DataDog/integrations-core/pull/2081
[64]: https://github.com/DataDog/integrations-core/pull/2067
[65]: https://github.com/DataDog/integrations-core/pull/2004
[66]: https://github.com/DataDog/integrations-core/pull/1957
[67]: https://github.com/DataDog/integrations-core/pull/1935
[68]: https://github.com/DataDog/integrations-core/pull/1927
[69]: https://github.com/DataDog/integrations-core/pull/1911
[70]: https://github.com/DataDog/integrations-core/pull/1880
[71]: https://github.com/DataDog/integrations-core/pull/1897
[72]: https://github.com/DataDog/integrations-core/pull/1875
[73]: https://github.com/DataDog/integrations-core/pull/1866
[74]: https://github.com/DataDog/integrations-core/pull/1790
[75]: https://github.com/DataDog/integrations-core/pull/1743
[76]: https://github.com/DataDog/integrations-core/pull/1734
[77]: https://github.com/DataDog/integrations-core/pull/1596
[78]: https://github.com/DataDog/integrations-core/pull/1652
[79]: https://github.com/DataDog/integrations-core/pull/1581
[80]: https://github.com/DataDog/integrations-core/pull/1565
[81]: https://github.com/DataDog/integrations-core/pull/1566
[82]: https://github.com/DataDog/integrations-core/pull/1561
[83]: https://github.com/DataDog/integrations-core/issues/1183
