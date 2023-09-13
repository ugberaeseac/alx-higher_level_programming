#!/usr/bin/node


exports.converter = function (base) {
  function convertBase (num) {
    return num.toString(base);
  }
  return convertBase;
};
