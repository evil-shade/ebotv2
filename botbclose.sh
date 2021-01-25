#!/bin/bash

# shellcheck disable=SC2046
kill $(ps aux | grep "firefox")

exit 0