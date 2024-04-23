#!/usr/bin/node

exports.converter = function (base) {
  function convertToBase (number) {
    return number.toString(base);
  }
  return convertToBase;
};
