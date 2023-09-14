#!/usr/bin/node

exports.esrever = function (list) {
  let listLength = list.length - 1;
  let i = 0;
  while (i < listLength) {
    const temp = list[listLength];
    list[listLength] = list[i];
    list[i] = temp;

    i++;
    listLength--;
  }
  return list;
};
