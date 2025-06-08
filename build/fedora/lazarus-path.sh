DIR="/usr/lib64/share/lazarus"
if ! echo "${PATH}" | grep -q "$DIR" ; then
    export PATH="$DIR:$PATH"
fi
