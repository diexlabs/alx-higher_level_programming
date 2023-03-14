#!/usr/bin/node

exports.addMeMaybe = function (n, func) {
  n += 1;
  func(n);
};
