# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest
from stackstate_checks.stubs import aggregator

try:
    from stackstate_checks.checks.win.winpdh_base import PDHBaseCheck

    from stackstate_test_libs.win.pdh_mocks import initialize_pdh_tests, pdh_mocks_fixture
except ImportError:
    pass

from .utils import requires_windows


DEFAULT_INSTANCE = {'host': '.'}

SINGLE_INSTANCE_COUNTER = [["Memory", None, "Available Bytes", "test.system.mem.available", "gauge"]]

INSTANCE_OF_SINGLE_INSTANCE_COUNTER = [["Memory", "1", "Available Bytes", "test.system.mem.available", "gauge"]]

MULTI_INSTANCE_COUNTER = [["Processor", None, "% Processor Time", "test.processor_time", "gauge"]]

MULTI_INSTANCE_COUNTER_WITH_INSTANCES = [
    ["Processor", "0", "% Processor Time", "test.processor_time_0", "gauge"],
    ["Processor", "1", "% Processor Time", "test.processor_time_1", "gauge"],
]


@requires_windows
def test_single_instance_counter(aggregator, pdh_mocks_fixture):  # noqa: F811
    initialize_pdh_tests()
    instance = DEFAULT_INSTANCE
    c = PDHBaseCheck("testcheck", {}, {}, [instance], SINGLE_INSTANCE_COUNTER)
    c.check(instance)

    aggregator.assert_metric("test.system.mem.available", tags=None, count=1)


@requires_windows
def test_single_instance_counter_with_instance(aggregator, pdh_mocks_fixture):  # noqa: F811
    initialize_pdh_tests()
    instance = DEFAULT_INSTANCE
    with pytest.raises(AttributeError):
        PDHBaseCheck("testcheck", {}, {}, [instance], INSTANCE_OF_SINGLE_INSTANCE_COUNTER)


@requires_windows
def test_multi_instance_counter(aggregator, pdh_mocks_fixture):  # noqa: F811
    initialize_pdh_tests()
    instance = DEFAULT_INSTANCE
    c = PDHBaseCheck("testcheck", {}, {}, [instance], MULTI_INSTANCE_COUNTER)
    c.check(instance)
    for t in ['instance:0', 'instance:1', 'instance:_Total']:
        aggregator.assert_metric("test.processor_time", tags=['%s' % t], count=1)
    assert aggregator.metrics_asserted_pct == 100.0


@requires_windows
def test_multi_instance_counter_specific_instances(aggregator, pdh_mocks_fixture):  # noqa: F811
    initialize_pdh_tests()
    instance = DEFAULT_INSTANCE
    c = PDHBaseCheck("testcheck", {}, {}, [instance], MULTI_INSTANCE_COUNTER_WITH_INSTANCES)
    c.check(instance)
    for t in ['test.processor_time_0', 'test.processor_time_1']:
        aggregator.assert_metric(t, tags=None, count=1)
    assert aggregator.metrics_asserted_pct == 100.0


@requires_windows
def test_returns_partial_metrics(aggregator, pdh_mocks_fixture):  # noqa: F811
    COUNTER_LIST = [
        ["NTDS", None, "LDAP Client Sessions", "active_directory.ldap.client_sessions", "gauge"],
        ["NTDS", None, "LDAP Bind Time", "active_directory.ldap.bind_time", "gauge"],
        ["NTDS", None, "LDAP Successful Binds/sec", "active_directory.ldap.successful_binds_persec", "gauge"],
        ["NTDS", None, "LDAP Searches/sec", "active_directory.ldap.searches_persec", "gauge"],
        # these two don't exist
        ["NTDS", None, "Kerberos Authentications/sec", "active_directory.kerberos.auths_persec", "gauge"],
        ["NTDS", None, "NTLM Authentications/sec", "active_directory.ntlm.auths_persec", "gauge"],
    ]
    initialize_pdh_tests()
    instance = DEFAULT_INSTANCE
    c = PDHBaseCheck("testcheck", {}, {}, [instance], COUNTER_LIST)
    c.check(instance)

    aggregator.assert_metric("active_directory.ldap.client_sessions", tags=None, count=1)
    aggregator.assert_metric("active_directory.ldap.bind_time", tags=None, count=1)
    aggregator.assert_metric("active_directory.ldap.successful_binds_persec", tags=None, count=1)
    aggregator.assert_metric("active_directory.ldap.searches_persec", tags=None, count=1)
    assert aggregator.metrics_asserted_pct == 100.0
