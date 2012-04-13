# 0runner

## A simple multi-launcher for 0install

The maintainer of [ZeroInstall](http://0install.net) has a
[philosophical objection](http://news.gmane.org/find-root.php?message_id=%3cCAG4opy%2dsh%2d%3dAjKpu5BRJCkE%2dgSHqKobXDepzVSS9tNbD%5fCJQjw%40mail.gmail.com%3e)
to allowing the direct expression in feed files of package build
instructions with multiple steps.  To get around this inconvenience,
`0runner` can be used to `0launch` a sequence of feeds, passing `;` as a
separator between lists of arguments to be passed to 0launch.  For
example, the following snippet issues two cmake commands in sequence:

```xml
<command name='compile'>
 <runner interface='http://ryppl.github.com/feeds/ryppl/0runner.xml'/>
   <arg>http://afb.users.sourceforge.net/zero-install/interfaces/cmake.xml</arg>
       <arg>-D</arg> <arg>CMAKE_INSTALL_PREFIX=${DISTDIR}</arg> <arg>${SRCDIR}</arg>
   <arg>;</arg>
   <arg>http://afb.users.sourceforge.net/zero-install/interfaces/cmake.xml</arg>
       <arg>--build</arg> <arg>.</arg> <arg>--target</arg> <arg>install</arg>
 </runner>
</command>
```
