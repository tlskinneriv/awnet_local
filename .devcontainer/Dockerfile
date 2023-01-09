ARG VARIANT

FROM mcr.microsoft.com/vscode/devcontainers/python:$VARIANT

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        # Additional library needed by some tests and accordingly by VScode Tests Discovery
        bluez \
        libudev-dev \
        libavformat-dev \
        libavcodec-dev \
        libavdevice-dev \
        libavutil-dev \
        libswscale-dev \
        libswresample-dev \
        libavfilter-dev \
        libpcap-dev \
        git \
        libffi-dev \
        libssl-dev \
        libjpeg-dev \
        zlib1g-dev \
        autoconf \
        build-essential \
        libopenjp2-7 \
        libtiff5 \
        libturbojpeg0 \
        tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /srv/homeassistant \
    && chown vscode:vscode /srv/homeassistant

COPY .devcontainer/setup.sh /srv/homeassistant/

RUN chown vscode:vscode /srv/homeassistant/setup.sh \
    && chmod 755 /srv/homeassistant/setup.sh

USER vscode

WORKDIR /srv/homeassistant

RUN python -m venv . \
    && source bin/activate \
    && python -m pip install wheel \
    && pip3 install homeassistant

RUN ./setup.sh

# WORKDIR /workspaces

# # Install Python dependencies from requirements
# COPY requirements.txt ./
# COPY homeassistant/package_constraints.txt homeassistant/package_constraints.txt
# RUN pip3 install -r requirements.txt
# COPY requirements_test.txt requirements_test_pre_commit.txt ./
# RUN pip3 install -r requirements_test.txt
# RUN rm -rf requirements.txt requirements_test.txt requirements_test_pre_commit.txt homeassistant/

# Set the default shell to bash instead of sh
ENV SHELL /bin/bash
