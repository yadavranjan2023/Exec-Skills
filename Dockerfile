# Exec-Skills governance image
#
# Bundles the executive SKILL.md manifests and the validate_skill.py
# linter into a single runnable image. Two uses:
#
#   1. CI/CD: pull this image in another repo's pipeline to validate
#      that manifests still pass their structural checks.
#   2. Agent runtime: mount or copy /manifests into an agent's context
#      so it always has a known-good, versioned copy of the governance
#      rules rather than fetching raw files at runtime.
#
# Build locally:
#   docker build -t exec-skills .
#
# Run the validator against the bundled manifests:
#   docker run --rm exec-skills
#
# Just read a manifest out of the image:
#   docker run --rm exec-skills cat /manifests/cto/CTO.SKILL.md

FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/yadavranjan2023/Exec-Skills"
LABEL org.opencontainers.image.description="Executive SKILL.md governance manifests and validator"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app

# Install the one dependency the validator needs.
RUN pip install --no-cache-dir pyyaml

# Copy the manifests into a clearly-named, stable path so anything
# consuming this image (CI job, agent, mounted volume) has a
# predictable location regardless of how the repo is organized.
COPY _base/ /manifests/_base/
COPY ceo/ /manifests/ceo/
COPY cto/ /manifests/cto/
COPY cpo/ /manifests/cpo/
COPY clo/ /manifests/clo/
COPY scripts/validate_skill.py /app/validate_skill.py

# Default behavior: validate every bundled manifest and exit non-zero
# on failure, so this works as a CI gate out of the box.
ENTRYPOINT ["python", "/app/validate_skill.py"]
CMD ["/manifests/_base/TheExecutiveSKILL.md", \
     "/manifests/ceo/CEO.SKILL.md", \
     "/manifests/cto/CTO.SKILL.md", \
     "/manifests/cpo/CPO.SKILL.md", \
     "/manifests/clo/CLO.SKILL.md"]
