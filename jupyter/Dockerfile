FROM archlinux/base
run pacman -Syu --noconfirm \
	base-devel \
	vim \
	git \
	python \
	python-pip \
	jupyterlab
WORKDIR /app
COPY . /app
WORKDIR /app
run pacman -U --noconfirm /app/builtPackages/*
ENTRYPOINT ["sh", "entrypoint.sh"]

