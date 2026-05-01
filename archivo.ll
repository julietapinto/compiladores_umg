; ModuleID = "programa"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 5, i32* %"x"
  %"x.1" = load i32, i32* %"x"
  %".3" = add i32 %"x.1", 3
  ret i32 0
}