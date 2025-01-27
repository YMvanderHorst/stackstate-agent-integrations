# (C) StackState 2022
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from stackstate_checks.splunk.config.splunk_instance_config import SplunkTelemetryInstanceConfig
from stackstate_checks.splunk.telemetry.splunk_telemetry import SplunkTelemetrySavedSearch, SplunkTelemetryInstance
from stackstate_checks.splunk.telemetry.splunk_telemetry_base import SplunkTelemetryBase

"""
    Events as generic events from splunk. StackState.
"""

DEFAULT_SETTINGS = {
    'default_request_timeout_seconds': 5,
    'default_search_max_retry_count': 3,
    'default_search_seconds_between_retries': 1,
    'default_verify_ssl_certificate': False,
    'default_batch_size': 1000,
    'default_saved_searches_parallel': 3,
    'default_initial_history_time_seconds': 0,
    'default_max_restart_history_seconds': 86400,
    'default_max_query_chunk_seconds': 300,
    'default_initial_delay_seconds': 0,
    'default_unique_key_fields': ["_time"],
    'default_app': "search",
    'default_parameters': {
        "force_dispatch": True,
        "dispatch.now": True
    }
}


class EventSavedSearch(SplunkTelemetrySavedSearch):
    last_events_at_epoch_time = set()

    def __init__(self, instance_config, saved_search_instance):
        super(EventSavedSearch, self).__init__(instance_config, saved_search_instance)

        self.optional_fields = {
            "event_type": "event_type",
            "source_type_name": "_sourcetype",
            "msg_title": "msg_title",
            "msg_text": "msg_text",
        }


class SplunkEvent(SplunkTelemetryBase):
    SERVICE_CHECK_NAME = "splunk.event_information"

    def __init__(self, name, init_config, agentConfig, instances=None):
        self.PERSISTENT_CACHE_KEY = "splunk_event"
        self.TRANSACTIONAL_PERSISTENT_CACHE_KEY = "splunk_event"
        super(SplunkEvent, self).__init__(name, init_config, agentConfig, instances)

    def _apply(self, **event_data):
        # msg_title, msg_text, event_type are required for event in Agent v2 to be created
        generic_event_text = "generic_splunk_event"
        if not event_data.get("msg_title"):
            event_data["msg_title"] = generic_event_text
        if not event_data.get("msg_text"):
            event_data["msg_text"] = generic_event_text
        if not event_data.get("event_type"):
            event_data["event_type"] = generic_event_text
        self.event(event_data)

    def get_instance(self, instance, current_time):
        metric_instance_config = SplunkTelemetryInstanceConfig(instance, self.init_config, DEFAULT_SETTINGS)

        def _create_saved_search(instance_config, saved_search_instance):
            return EventSavedSearch(instance_config, saved_search_instance)

        telemetry_instance = SplunkTelemetryInstance(current_time, instance, metric_instance_config,
                                                     _create_saved_search)
        return telemetry_instance
