FROM archlinux/base
run pacman -Syu --noconfirm \
	base-devel \
	vim \
	git \
	python \
	python-pip \ 
	python-flask \
	python-flask-login \
	python-redis \
	gunicorn
#COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
#RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
run pacman -U --noconfirm /app/builtPackages/*
ENTRYPOINT ["sh", "entrypoint.sh"]
