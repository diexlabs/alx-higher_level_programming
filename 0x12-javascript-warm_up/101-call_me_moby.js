#!/usr/bin/node

exports.callMeMoby = function (n, func) {
  let i = 0;
  while (i < n) {
    func();
    i++;
  }
};
