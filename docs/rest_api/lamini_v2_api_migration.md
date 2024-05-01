# 10/5/23 - Migrating from Lamini V1 API to V2 API 

Lamini has migrated all inference and training services to its V2 Rest API. In this migration the following notable breaking changes have been made:

* Updated completions, training, etc REST api from `/v1` to `/v2`.
    * Simplified REST API required arguments to be dead-simple json objects, based on customer feedback.
    * Removed support for `list` and `dict` types for improved api stability.
    * `/v1` api is no longer supported.
* Updated python SDK version from major version 0 to major version 1 (1.0.0)
* Cleared all datasets saved via the `/v1/data` api
* Updated python SDK to include a new class `Lamini` accessible by `from lamini import Lamini`. 
    * This class operates on python dictionaries, as opposed to Lamini Types.
    * `LLMEngine` still supports Lamini Types, and is the basis for all of Lamini's `Runner` classes. This class is migrated to use the `/v2` api.
* Added a `LaminiClassifier` class to help users train their own classes. 

Thank you for all your support and feedback! 