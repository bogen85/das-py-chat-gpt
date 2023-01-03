program dot_vars;

uses
  sysutils;

const
  endl = lineEnding;

procedure main;
  var
    i: integer;
    pvar: string;
  begin
    for i := 0 to paramCount() do begin
      pvar := paramStr(i);
      writeln(format('%s%s%-4s%s', [pvar, endl, ':', getEnvironmentVariable(pvar)]));
    end;
  end;

begin
  main;
end.
// CudaText: lexer_file=Pascal; tab_size=2; tab_spaces=Yes; newline=LF;
