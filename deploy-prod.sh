#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

IMAGE=$(grep -E '^[[:space:]]*image:' yoink.yaml | head -1 | awk '{print $2}')
SERVICE=monty-django
PLATFORM=${PLATFORM:-linux/amd64}

#BRANCH=$(git rev-parse --abbrev-ref HEAD)
#if [ "$BRANCH" != "main" ]; then
  #echo "error: prod deploys must run from 'main' (on '$BRANCH')" >&2
  #exit 1
#fi

#if [ -n "$(git status --porcelain)" ]; then
  #echo "error: working tree is dirty (stash any WIP)" >&2
  #exit 1
#fi

TAG=$(git rev-parse --short HEAD)
#if ! git merge-base --is-ancestor HEAD "@{upstream}" 2>/dev/null; then
  #echo "error: HEAD is not pushed/merged to its upstream" >&2
  #exit 1
#fi

if [ -n "$(git status --porcelain)" ]; then
  TAG="${TAG}-dirty-$(date +%H%M%S)"
fi

docker buildx build --platform "$PLATFORM" -t "${IMAGE}:${TAG}" --push .
yoink up --service "${SERVICE}" --tag "${SERVICE}=${TAG}"
