FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# The base image ships a Yarn apt source with an expired signing key, which makes
# `apt-get update` (and so the desktop-lite feature) fail. Yarn isn't needed here.
RUN rm -f /etc/apt/sources.list.d/yarn.list
