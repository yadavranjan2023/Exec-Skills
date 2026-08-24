# Exec-Skills governance image
#
# Bundles the executive governance reference manifests and the
# validate_skill.py linter into a single runnable image.
#
# Build locally:
#   docker build -t exec-skills .
#
# Run the validator against the bundled manifests:
#   docker run --rm exec-skills

FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/yadavranjan2023/Exec-Skills"
LABEL org.opencontainers.image.description="Executive SKILL.md governance manifests and validator"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app

RUN pip install --no-cache-dir pyyaml

COPY skills/exec-skills-governance/references/ /manifests/
COPY skills/exec-skills-governance/scripts/validate_skill.py /app/validate_skill.py

ENTRYPOINT ["python", "/app/validate_skill.py"]
CMD ["/manifests/base.md", \
     "/manifests/ceo.md", \
     "/manifests/cto.md", \
     "/manifests/cpo.md", \
     "/manifests/clo.md"]
