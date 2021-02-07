# Python code @beducode
 

import base64, codecs
magic = 'ZnJvbSBwcmV0dHl0YWJsZSBpbXBvcnQgUHJldHR5VGFibGUNCmZyb20gb3MgaW1wb3J0IHN5c3RlbSwgbmFtZQ0KaW1wb3J0IHJlcXVlc3RzDQppbXBvcnQganNvbg0KaW1wb3J0IHRpbWUNCmltcG9ydCBzeXMNCmltcG9ydCByYW5kb20NCmltcG9ydCBvcw0KaW1wb3J0IGFyZ3BhcnNlDQppbXBvcnQgY29sb3JhbWENCmltcG9ydCBzdHJpbmcNCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUsIEJhY2ssIFN0eWxlDQpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludA0KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUNCmltcG9ydCBweXNob3J0ZW5lcnMNCmZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IFJlcXVlc3QsIHVybG9wZW4NCmZyb20gaW5wdXRpbWVvdXQgaW1wb3J0IGlucHV0aW1lb3V0LCBUaW1lb3V0T2NjdXJyZWQNCmNvbG9yYW1hLmluaXQoYXV0b3Jlc2V0PVRydWUpDQoNCiMgQ09ORklHIFdBUk5BDQpyZXMgPSBTdHlsZS5SRVNFVF9BTEwNCmhpamF1ID0gU3R5bGUuTk9STUFMK0ZvcmUuR1JFRU4NCmhpamF1MiA9IFN0eWxlLkJSSUdIVCtGb3JlLkdSRUVODQptZXJhaCA9IFN0eWxlLk5PUk1BTCtGb3JlLlJFRA0KbWVyYWgyID0gU3R5bGUuQlJJR0hUK0ZvcmUuUkVEDQprdW5pbmcgPSBTdHlsZS5OT1JNQUwrRm9yZS5ZRUxMT1cNCmt1bmluZzIgPSBTdHlsZS5CUklHSFQrRm9yZS5ZRUxMT1cNCmJpcnUgPSBTdHlsZS5OT1JNQUwrRm9yZS5CTFVFDQpiaXJ1MiA9IFN0eWxlLkJSSUdIVCtGb3JlLkJMVUUNCnB1dGloID0gU3R5bGUuTk9STUFMK0ZvcmUuV0hJVEUNCnB1dGloMiA9IFN0eWxlLkJSSUdIVCtGb3JlLldISVRFDQoNCiMgQ09ORklHIEJBQ0tHUk9VTkQNCmJhY2ttZXJhaCA9IFN0eWxlLkJSSUdIVCtCYWNrLlJFRCtGb3JlLkJMQUNLDQpiYWNraGlqYXUgPSBTdHlsZS5CUklHSFQrQmFjay5HUkVFTitGb3JlLldISVRFDQpiYWNra3VuaW5nID0gU3R5bGUuQlJJR0hUK0JhY2suWUVMTE9XK0ZvcmUuQkxBQ0sNCmJhY2tiaXJ1ID0gU3R5bGUuQlJJR0hUK0JhY2suQkxVRStGb3JlLldISVRFDQpiYWNrcHV0aWggPSBTdHlsZS5CUklHSFQrQmFjay5XSElURStGb3JlLkJMQUNLDQoNCiMgQkFOTkVSDQoNCmRlZiBiYW5uZXIoKToNCiAgICBiYW5uZXIgPSAiXG5cbiINCiAgICBiYW5uZXIgPSBiYW5uZXIgKyBiaXJ1MiArICIgX19fX18gXyAgICAgICAgICAgICAgICAgICDigIFcbiINCiAgICBiYW5uZXIgPSBiYW5uZXIgKyAiL19fICAgKF8pIF9fXyAgXyBfXyAgIF9fIF8gICAiICsgIlxuIg0KICAgIGJhbm5lciA9IGJhbm5lciArICIgIC8gL1wvIHwvIF8gXHwgJ18gXCAvIF9gIHzigIHigIFcbiINCiAgICBiYW5uZXIgPSBiYW5uZXIgKyAiIC8gLyAgfCB8IChfKSB8IHwgfCB8IChffCB84oCBIFxuIg0KICAgIGJhbm5lciA9IGJhbm5lciArICIgXC8gICB8X3xcX19fL3xffCB8X3xcX18sIHzigIFcbiINCiAgICBiYW5uZXIgPSBiYW5uZXIgKyAiICAgICAgICAgICAgICAgICAgICAgfF9fXy8g4oCBXG4iDQogICAgYmFubmVyID0gYmFubmVyICsgcHV0aWgyICsgXA0KICAgICAgICAiSW5mb3JtYXNpIHVwZGF0ZSBoYXJnYSBjb2luIHJlYWwgdGltZSBwZXIgMTAgZGV0aWsgZGFyaSBpbmRvZGF4XG5cbiINCiAgICBiYW5uZXIgPSBiYW5uZXIgKyBiaXJ1MiArICJTdW1iZXIgaGFyZ2EgIDogIg0KICAgIGJhbm5lciA9IGJhbm5lciArIHB1dGloMiArICJpbmRvZGF4LmNvbVxuIg0KICAgIGJhbm5lciA9IGJhbm5lciArIGJpcnUyICsgIkF1dGhvciAgICAgICAgOiAiDQogICAgYmFubmVyID0gYmFubmVyICsgcHV0aWgyICsgImdpdGh1YkBiZWR1Y29kZVxuIg0KICAgIGJhbm5lciA9IGJhbm5lciArIGJpcnUyICsgIkNvbnRhY3QgICAgICAgOiAiDQogICAgYmFubmVyID0gYmFubmVyICsgcHV0aWgyICsgIkBiZWR1cGxheSAvI'
love = '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'
god = '9pbihjdXJyKToNCiAgICBhcGkgPSAnaHR0cHM6Ly9pbmRvZGF4LmNvbS9hcGkvJyArIHN0cihjdXJyKS5sb3dlcigpICsgIl9pZHIiICsgJy90aWNrZXInDQogICAgcmVxID0gcmVxdWVzdHMuZ2V0KGFwaSkNCiAgICBkYXRhID0ganNvbi5sb2FkcyhyZXEudGV4dCkNCiAgICBpZiAnZXJyb3InIGluIGRhdGE6DQogICAgICAgIGNsZWFyKCkNCiAgICAgICAgdmFsaWRhc2lrb2luKGN1cnIpDQogICAgZWxzZToNCiAgICAgICAgcGFzcw0KDQojIE1FTlUgU1BFU0lGSUMgTUFSS0VUDQpkZWYgY2VraGFyZ2EocGFpcixzcCk6DQogICAgbGlzdHBhaXIgPSBbXQ0KICAgIA0KICAgIGlmIHNwID09IDA6DQogICAgICAgIHBhaXIgPSBwYWlyLnNwbGl0KCkNCiAgICAgICAgbGVucGFpciA9IGxlbihwYWlyKQ0KICAgIA0KICAgICAgICBmb3IgaSBpbiByYW5nZShsZW5wYWlyKToNCiAgICAgICAgICAgIGNla2NvaW4ocGFpcltpXSkNCiAgICAgICAgICAgIGxpc3RwYWlyLmFwcGVuZChwYWlyW2ldKQ0KICAgIGVsc2U6DQogICAgICAgIGxpc3RwYWlyID0gcGFpcg0KICAgICAgICANCiAgICB0YWJsZWR0ID0gUHJldHR5VGFibGUoKQ0KICAgIHRhYmxlZHQuZmllbGRfbmFtZXMgPSBbIk5PLiIsIGt1bmluZyArICJLT0lOIiArIHJlcywgaGlqYXUyICsgIkhBUkdBIFRFUlRJTkdJIiArIHJlcywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXJhaDIgKyAiSEFSR0EgVEVSRU5EQUgiICsgcmVzLCAiSEFSR0EgKElEUikiLCBoaWphdSArICJCRUxJIiArIHJlcywgbWVyYWggKyAiSlVBTCIgKyByZXNdDQogICAgDQogICAgbGlzdHBhaXIgPSBsaXN0KGRpY3QuZnJvbWtleXMobGlzdHBhaXIpKQ0KICAgIGdldGNvaW4gPSBsZW4obGlzdHBhaXIpDQogICAgDQogICAgZm9yIHggaW4gcmFuZ2UoZ2V0Y29pbik6DQogICAgICAgIGFwaSA9ICdodHRwczovL2luZG9kYXguY29tL2FwaS8nICsgc3RyKGxpc3RwYWlyW3hdKS5sb3dlcigpICsgIl9pZHIiICsgJy90aWNrZXInDQogICAgICAgIHJlcSA9IHJlcXVlc3RzLmdldChhcGkpDQogICAgICAgIGRhdGEgPSBqc29uLmxvYWRzKHJlcS50ZXh0KQ0KDQogICAgICAgIHRhYmxlZHQuYWRkX3JvdyhbYmlydTIgKyBzdHIoeCsxKSArIHJlcywNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBzdHIobGlzdHBhaXJbeF0pLnVwcGVyKCksDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgcnVwaWFoX2Zvcm1hdChpbnQoZGF0YVsndGlja2VyJ11bJ2hpZ2gnXSkpLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJ1cGlhaF9mb3JtYXQoaW50KGRhdGFbJ3RpY2tlciddWyJsb3ciXSkpLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHJ1cGlhaF9mb3JtYXQoaW50KGRhdGFbJ3RpY2tlciddWyJsYXN0Il0pKSwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBydXBpYWhfZm9ybWF0KGludChkYXRhWyd0aWNrZXInXVsiYnV5Il0pKSwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBydXBpYWhfZm9ybWF0KGludChkYXRhWyd0aWNrZXInXVsic2VsbCJdKSkNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBdKQ0KDQogICAgYmFubmVyKCkNCiAgICBwcmludCgiXG4iKQ0KICAgIHByaW50KHRhYmxlZHQpDQogICAgICAgIA0KICAgIA0KICAgIHRyeToNCiAgICAgICAgY21kbWFya2V0ID0gYmlydTIgKyAnXHInICsgcHV0aWgyICsgJz4+ICcgKyByZXMgKyBiaXJ1MiArICdUZWthbiBUb21ib2wgRW50ZXIgVW50dWsgS2VtYmFsaSBLZSBNZW51IFV0YW1hJw0KICAgICAgICBob21lID0gaW5wdXRpbWVvdXQocHJvbXB0PWNtZG1hcmtldCwgdGltZW91dD1pbnRlcnZsKQ0KICAgICAgICBpZiBob21lID09ICIiOg0KICAgICAgICAgICAgY2xlYXIoKQ0KICAgICAgICAgICAgbWFpbigpDQogICAgZXh'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))