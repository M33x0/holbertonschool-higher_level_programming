#!/usr/bin/node
exports.addMeMaybe = function (number, func) {
  number += 1;
  func(number);
};
