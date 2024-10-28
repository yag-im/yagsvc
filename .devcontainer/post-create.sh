#!/usr/bin/env bash

mkdir -p /workspaces/yagsvc/.vscode
cp /workspaces/yagsvc/.devcontainer/vscode/* /workspaces/yagsvc/.vscode

make bootstrap
