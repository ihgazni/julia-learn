pip3 uninstall julia-learn
git rm -r dist
git rm -r build
git rm -r julia-learn.egg-info
rm -r dist
rm -r build
rm -r julia-learn.egg-info
git add .
git commit -m "remove old build"

