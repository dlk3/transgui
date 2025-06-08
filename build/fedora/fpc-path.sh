DIR="/usr/lib64/fpc/3.2.4"
if ! echo "${PATH}" | grep -q "$DIR" ; then
    export PATH="$DIR:$PATH"
fi
