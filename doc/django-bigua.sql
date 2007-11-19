-- phpMyAdmin SQL Dump
-- version 2.11.2deb2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 19, 2007 at 04:54 PM
-- Server version: 5.0.45
-- PHP Version: 5.2.4-2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `bigua`
--

--
-- Dumping data for table `auth_group`
--


--
-- Dumping data for table `auth_group_permissions`
--


--
-- Dumping data for table `auth_message`
--


--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add message', 1, 'add_message'),
(2, 'Can change message', 1, 'change_message'),
(3, 'Can delete message', 1, 'delete_message'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add permission', 4, 'add_permission'),
(11, 'Can change permission', 4, 'change_permission'),
(12, 'Can delete permission', 4, 'delete_permission'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add site', 7, 'add_site'),
(20, 'Can change site', 7, 'change_site'),
(21, 'Can delete site', 7, 'delete_site'),
(22, 'Can add log entry', 8, 'add_logentry'),
(23, 'Can change log entry', 8, 'change_logentry'),
(24, 'Can delete log entry', 8, 'delete_logentry'),
(25, 'Can add menu', 9, 'add_menu'),
(26, 'Can change menu', 9, 'change_menu'),
(27, 'Can delete menu', 9, 'delete_menu'),
(28, 'Can add link', 10, 'add_link'),
(29, 'Can change link', 10, 'change_link'),
(30, 'Can delete link', 10, 'delete_link'),
(31, 'Can add club', 11, 'add_club'),
(32, 'Can change club', 11, 'change_club'),
(33, 'Can delete club', 11, 'delete_club'),
(34, 'Can add reserva', 12, 'add_reserva'),
(35, 'Can change reserva', 12, 'change_reserva'),
(36, 'Can delete reserva', 12, 'delete_reserva'),
(37, 'Can add cancha', 13, 'add_cancha'),
(38, 'Can change cancha', 13, 'change_cancha'),
(39, 'Can delete cancha', 13, 'delete_cancha'),
(65, 'Can change club translation', 22, 'change_clubtranslation'),
(64, 'Can add club translation', 22, 'add_clubtranslation'),
(43, 'Can add registro', 15, 'add_registro'),
(44, 'Can change registro', 15, 'change_registro'),
(45, 'Can delete registro', 15, 'delete_registro'),
(46, 'Can add lista de espera', 16, 'add_listadeespera'),
(47, 'Can change lista de espera', 16, 'change_listadeespera'),
(48, 'Can delete lista de espera', 16, 'delete_listadeespera'),
(49, 'Can add cancha inhabilitada', 17, 'add_canchainhabilitada'),
(50, 'Can change cancha inhabilitada', 17, 'change_canchainhabilitada'),
(51, 'Can delete cancha inhabilitada', 17, 'delete_canchainhabilitada'),
(52, 'Can add sancion', 18, 'add_sancion'),
(53, 'Can change sancion', 18, 'change_sancion'),
(54, 'Can delete sancion', 18, 'delete_sancion'),
(55, 'Can add cuota', 19, 'add_cuota'),
(56, 'Can change cuota', 19, 'change_cuota'),
(57, 'Can delete cuota', 19, 'delete_cuota'),
(58, 'Can add socio', 20, 'add_socio'),
(59, 'Can change socio', 20, 'change_socio'),
(60, 'Can delete socio', 20, 'delete_socio'),
(61, 'Can add configuracion', 21, 'add_configuracion'),
(62, 'Can change configuracion', 21, 'change_configuracion'),
(63, 'Can delete configuracion', 21, 'delete_configuracion'),
(66, 'Can delete club translation', 22, 'delete_clubtranslation'),
(67, 'Can add sancion translation', 23, 'add_sanciontranslation'),
(68, 'Can change sancion translation', 23, 'change_sanciontranslation'),
(69, 'Can delete sancion translation', 23, 'delete_sanciontranslation'),
(70, 'Can add cuota translation', 24, 'add_cuotatranslation'),
(71, 'Can change cuota translation', 24, 'change_cuotatranslation'),
(72, 'Can delete cuota translation', 24, 'delete_cuotatranslation'),
(73, 'Can add cancha translation', 25, 'add_canchatranslation'),
(74, 'Can change cancha translation', 25, 'change_canchatranslation'),
(75, 'Can delete cancha translation', 25, 'delete_canchatranslation'),
(84, 'Can delete flat page', 28, 'delete_flatpage'),
(83, 'Can change flat page', 28, 'change_flatpage'),
(82, 'Can add flat page', 28, 'add_flatpage'),
(79, 'Can add cancha inhabilitada translation', 27, 'add_canchainhabilitadatranslation'),
(80, 'Can change cancha inhabilitada translation', 27, 'change_canchainhabilitadatranslation'),
(81, 'Can delete cancha inhabilitada translation', 27, 'delete_canchainhabilitadatranslation'),
(85, 'Can add invitado', 29, 'add_invitado'),
(86, 'Can change invitado', 29, 'change_invitado'),
(87, 'Can delete invitado', 29, 'delete_invitado');

--
-- Dumping data for table `auth_user_groups`
--


--
-- Dumping data for table `auth_user_user_permissions`
--


--
-- Dumping data for table `canchas_cancha`
--

INSERT INTO `canchas_cancha` (`id`, `club_id`, `costo`, `desactivada`) VALUES
(1, 1, 150.00, 0),
(2, 1, 250.00, 0);

--
-- Dumping data for table `canchas_canchainhabilitada`
--


--
-- Dumping data for table `canchas_canchainhabilitadatranslation`
--


--
-- Dumping data for table `canchas_canchatranslation`
--

INSERT INTO `canchas_canchatranslation` (`id`, `nombre`, `language_id`, `master_id`) VALUES
(1, 'La buena', 1, 1),
(2, 'The good one', 2, 1),
(3, 'La VIP', 1, 2),
(4, 'The VIP', 2, 2);

--
-- Dumping data for table `canchas_club`
--

INSERT INTO `canchas_club` (`id`, `nombre`, `sitio_id`) VALUES
(1, 'Biguá', 3);

--
-- Dumping data for table `canchas_clubtranslation`
--

INSERT INTO `canchas_clubtranslation` (`id`, `direccion`, `language_id`, `master_id`) VALUES
(1, '21 de setiembre 987', 1, 1),
(2, 'September 21st Street 987', 2, 1);

--
-- Dumping data for table `canchas_configuracion`
--

INSERT INTO `canchas_configuracion` (`id`, `clave`, `valor`, `core`) VALUES
(1, 'cancelar_antes_de', '120', 1);

--
-- Dumping data for table `canchas_cuota`
--

INSERT INTO `canchas_cuota` (`id`, `mes`, `ano`) VALUES
(1, 12, 2007);

--
-- Dumping data for table `canchas_cuotatranslation`
--

INSERT INTO `canchas_cuotatranslation` (`id`, `observaciones`, `language_id`, `master_id`) VALUES
(1, '', 1, 1),
(2, '', 2, 1);

--
-- Dumping data for table `canchas_invitado`
--

INSERT INTO `canchas_invitado` (`id`, `nombre`, `documento`) VALUES
(1, 'Invitado', 'N/A'),
(2, 'Alvaro ', '4.128476-2'),
(3, 'Alvaro ', '4.128476-2'),
(4, 'Alvaro ', '4.128476-2'),
(5, 'Alvaro ', '4.128476-2'),
(6, 'Alvaro ', '4.128476-2'),
(7, 'Alvaro ', '4.128476-2'),
(8, 'Alvaro ', '4.128476-2'),
(9, 'Alvaro ', '4.128476-2'),
(10, 'Marcelo Sosa', '123');

--
-- Dumping data for table `canchas_listadeespera`
--


--
-- Dumping data for table `canchas_registro`
--


--
-- Dumping data for table `canchas_reserva`
--

INSERT INTO `canchas_reserva` (`id`, `socio_id`, `cancha_id`, `content_type_id`, `object_id`, `desde`, `permitir_admin_cancelar`, `marca_temporal`, `cancelada`, `cancelada_por`, `cancelada_el`) VALUES
(1, 1, 1, 29, 1, '2007-11-19 10:00:00', 1, '2007-11-19 00:05:21', 1, 'Alvaro Mouriño', '2007-11-19 01:29:00'),
(2, 1, 1, 3, 2, '2007-11-20 10:00:00', 1, '2007-11-19 01:31:32', 1, 'Daniel Alaniz', '2007-11-19 01:54:48'),
(3, 3, 1, 3, 1, '2007-11-20 11:00:00', 1, '2007-11-19 01:57:36', 1, 'Ana Britos', '2007-11-19 02:37:46'),
(4, 1, 1, 3, 2, '2007-11-19 09:00:00', 1, '2007-11-19 03:00:37', 1, 'Alvaro Mouriño', '2007-11-19 03:55:58'),
(5, 1, 1, 3, 2, '2007-11-19 22:00:00', 0, '2007-11-19 04:05:46', 0, 'Alvaro Mouriño', '2007-11-19 18:20:47');

--
-- Dumping data for table `canchas_sancion`
--


--
-- Dumping data for table `canchas_sanciontranslation`
--


--
-- Dumping data for table `canchas_socio`
--

INSERT INTO `canchas_socio` (`id`, `user_id`, `cedula`, `domicilio`, `numero_de_socio`, `fecha_de_nacimiento`, `sexo`, `vencimiento_ficha_medica`, `ultima_cuota_paga_id`) VALUES
(1, 1, '4.123666-2', 'Mercedes y Cuareim', 123, '1984-12-06', 'M', '2009-11-13', 1),
(2, 2, '123', 'aaa', 122, '1980-11-13', 'M', '2009-11-13', 1),
(3, 3, '4.123666-2', 'Mercedes y Cuareim', 124, '1980-11-13', 'F', '2009-11-13', 1);

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2007-10-09 22:52:23', 1, 3, '1', 'alvaro', 2, 'Changed e-mail address, staff status, active and superuser status.'),
(2, '2007-10-09 23:02:53', 1, 7, '1', 'soma.com', 2, 'Changed domain name and display name.'),
(3, '2007-10-09 23:03:11', 1, 7, '1', 'soma.com.uy', 2, 'Changed domain name and display name.'),
(4, '2007-10-10 16:02:15', 1, 11, '1', 'Soma', 1, ''),
(5, '2007-10-10 16:08:21', 1, 13, '1', 'Marcelo Sosa (1)', 2, 'Changed Nombre and Desactivar.'),
(6, '2007-10-10 16:09:15', 1, 13, '2', '2 (El canchón)', 1, ''),
(7, '2007-10-10 16:13:42', 1, 13, '3', '3 (Julio Sosa)', 1, ''),
(8, '2007-10-30 17:59:31', 1, 11, '1', 'Soma', 1, ''),
(9, '2007-10-30 17:59:38', 1, 13, '1', '1 ()', 1, ''),
(10, '2007-10-30 18:01:42', 1, 13, '2', '2 (El canchón)', 1, ''),
(11, '2007-10-30 18:04:42', 1, 11, '1', 'Soma', 1, ''),
(12, '2007-10-30 18:05:45', 1, 13, '1', '1 (El canchón)', 1, ''),
(13, '2007-11-01 13:58:23', 1, 7, '3', 'bigua.com.uy', 1, ''),
(14, '2007-11-01 13:58:26', 1, 11, '1', 'Biguá', 1, ''),
(15, '2007-11-01 14:40:28', 1, 13, '1', '1 (El canchón)', 1, ''),
(16, '2007-11-04 21:54:47', 1, 11, '1', 'Biguá', 2, 'Added club translation "ClubTranslation object, language_code=es" and club translation "ClubTranslation object, language_code=en".'),
(17, '2007-11-06 17:07:35', 1, 9, '1', 'Principal', 1, ''),
(18, '2007-11-06 17:09:21', 1, 10, '1', 'Inicio', 1, ''),
(19, '2007-11-06 17:09:55', 1, 10, '1', 'Inicio', 2, 'Changed dirección and desactivar.'),
(20, '2007-11-06 17:17:35', 1, 9, '1', 'Principal', 2, 'No fields changed.'),
(21, '2007-11-06 17:28:30', 1, 10, '2', 'Reservar', 1, ''),
(22, '2007-11-06 17:28:47', 1, 10, '3', 'Lista de Espera', 1, ''),
(23, '2007-11-06 17:29:33', 1, 10, '4', 'Notificaciones', 1, ''),
(24, '2007-11-06 17:30:06', 1, 10, '5', 'Contacto', 1, ''),
(25, '2007-11-06 17:30:18', 1, 9, '1', 'Principal', 2, 'No fields changed.'),
(26, '2007-11-09 14:41:30', 1, 3, '1', 'alvaro', 2, 'Changed first name, last name, staff status, active and superuser status.'),
(27, '2007-11-12 01:41:03', 1, 11, '1', 'Biguá', 1, ''),
(28, '2007-11-12 02:00:02', 1, 13, '8', '8 (None)', 3, ''),
(29, '2007-11-12 02:00:10', 1, 13, '7', '7 (None)', 3, ''),
(30, '2007-11-12 02:00:16', 1, 13, '6', '6 (None)', 3, ''),
(31, '2007-11-12 02:00:23', 1, 13, '5', '5 (None)', 3, ''),
(32, '2007-11-12 02:00:33', 1, 13, '4', '4 (None)', 3, ''),
(33, '2007-11-12 02:00:39', 1, 13, '3', '3 (None)', 3, ''),
(34, '2007-11-12 02:00:46', 1, 13, '2', '2 (None)', 3, ''),
(35, '2007-11-12 02:02:41', 1, 13, '1', 'a', 2, 'Changed Desactivar.'),
(36, '2007-11-12 02:02:54', 1, 13, '1', 'The big court', 2, 'Changed Desactivar, <django.utils.functional.__proxy__ object at 0x106ff50> for cancha translation "CanchaTranslation object, language_code=es" and <django.utils.functional.__proxy__ object at 0x106ff50> for cancha translation "CanchaTranslation object, language_code=en".'),
(37, '2007-11-12 02:07:51', 1, 13, '9', 'The good one', 2, 'Added cancha translation "CanchaTranslation object, language_code=es" and cancha translation "CanchaTranslation object, language_code=en". Changed Desactivar.'),
(38, '2007-11-12 02:07:54', 1, 13, '9', 'The good one', 2, 'Changed Desactivar.'),
(39, '2007-11-12 17:06:56', 1, 12, '1', 'Reserva', 1, ''),
(40, '2007-11-12 19:49:04', 1, 13, '10', 'The poor one', 2, 'Added cancha translation "CanchaTranslation object, language_code=es" and cancha translation "CanchaTranslation object, language_code=en". Changed Desactivar.'),
(41, '2007-11-12 19:51:03', 1, 10, '2', 'Reservar', 2, 'Changed dirección and desactivar.'),
(42, '2007-11-12 19:51:12', 1, 10, '1', 'Inicio', 2, 'Changed dirección and desactivar.'),
(43, '2007-11-13 07:22:05', 1, 19, '1', 'Cuota object', 1, ''),
(44, '2007-11-13 07:23:33', 1, 20, '1', 'Socio object', 1, ''),
(45, '2007-11-13 07:38:02', 1, 12, '2', 'Reserva', 3, ''),
(46, '2007-11-13 21:54:57', 1, 13, '10', 'La de los pobres', 2, 'Changed Desactivar.'),
(47, '2007-11-13 22:35:21', 1, 3, '2', 'lore', 2, 'Changed first name, last name, e-mail address, staff status, active and superuser status.'),
(48, '2007-11-13 22:35:55', 1, 20, '2', 'lore', 1, ''),
(49, '2007-11-13 23:14:05', 1, 10, '3', 'Lista de Espera', 2, 'Changed desactivar.'),
(50, '2007-11-13 23:14:21', 1, 10, '3', 'Lista de Espera', 2, 'Changed desactivar.'),
(51, '2007-11-18 02:52:40', 1, 10, '6', 'Zona Restringida', 1, ''),
(52, '2007-11-18 02:52:54', 1, 9, '1', 'Principal', 2, 'No fields changed.'),
(53, '2007-11-18 21:14:35', 1, 20, '1', 'alvaro', 1, ''),
(54, '2007-11-18 21:18:42', 1, 20, '1', 'lore', 2, 'Modificado user.'),
(55, '2007-11-18 21:44:39', 1, 20, '1', 'alvaro', 2, 'Modificado user.'),
(56, '2007-11-18 22:37:31', 1, 13, '1', 'La buena', 1, ''),
(57, '2007-11-18 22:37:46', 1, 13, '2', 'La VIP', 1, ''),
(58, '2007-11-18 22:49:32', 1, 3, '2', 'danny', 2, 'Modificado nombre de usuario, nombre, apellidos, dirección de correo, es staff, activo y es superusuario.'),
(59, '2007-11-18 23:32:11', 1, 12, '2', 'Reserva', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(60, '2007-11-19 00:01:15', 1, 12, '2', 'Reserva', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(61, '2007-11-19 00:05:21', 1, 12, '1', 'Reserva', 1, ''),
(62, '2007-11-19 00:13:16', 1, 12, '1', 'Reserva', 2, 'Modificado Administrador puede cancelar, Cancelar y Cancelada por.'),
(63, '2007-11-19 00:32:02', 2, 20, '2', 'danny', 1, ''),
(64, '2007-11-19 01:26:40', 1, 12, '1', 'Reserva', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(65, '2007-11-19 01:28:07', 1, 12, '1', 'Reserva', 2, 'Modificado Administrador puede cancelar, Cancelar y Cancelada por.'),
(66, '2007-11-19 01:28:54', 1, 12, '1', 'Reserva', 2, 'Modificado Administrador puede cancelar, Cancelar y Cancelada por.'),
(67, '2007-11-19 01:56:26', 1, 3, '3', 'ana', 2, 'Modificado nombre, apellidos, dirección de correo, es staff, activo y es superusuario.'),
(68, '2007-11-19 01:57:21', 1, 20, '3', 'ana', 1, ''),
(69, '2007-11-19 04:49:12', 1, 28, '1', '/acerca/ -- Acerca de...', 1, ''),
(70, '2007-11-19 04:49:46', 1, 10, '5', 'Acerca de...', 2, 'Modificado nombre, pagina, dirección y desactivar.'),
(71, '2007-11-19 05:03:43', 1, 7, '1', 'localhost:8000', 2, 'Modificado nombre de dominio y nombre para mostrar.'),
(72, '2007-11-19 05:04:38', 1, 28, '1', '/acerca/ -- Acerca de...', 2, 'Modificado admitir comentarios y debe estar registrado.'),
(73, '2007-11-19 05:04:58', 1, 28, '1', '/acerca/ -- Acerca de...', 2, 'Modificado contenido, admitir comentarios y debe estar registrado.'),
(74, '2007-11-19 05:08:47', 1, 28, '1', '/acerca/ -- Acerca de...', 2, 'Modificado contenido, admitir comentarios y debe estar registrado.'),
(75, '2007-11-19 05:09:07', 1, 28, '1', '/acerca/ -- Acerca de...', 2, 'Modificado contenido, admitir comentarios y debe estar registrado.'),
(76, '2007-11-19 05:41:06', 2, 3, '2', 'danny', 2, 'Modificado es staff, activo y es superusuario.'),
(77, '2007-11-19 16:00:49', 1, 12, '5', 'alvaro con danny a las 11:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(78, '2007-11-19 16:05:54', 1, 12, '5', 'alvaro con danny a las 11:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(79, '2007-11-19 16:07:06', 1, 12, '5', 'alvaro con danny a las 11:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(80, '2007-11-19 16:07:53', 1, 12, '5', 'alvaro con danny a las 11:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(81, '2007-11-19 17:24:13', 1, 21, '1', 'cancelar_antes_de: 120', 1, ''),
(82, '2007-11-19 18:09:59', 1, 12, '5', 'alvaro con danny a las 11:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(83, '2007-11-19 18:10:31', 1, 12, '5', 'alvaro con danny a las 22:00 hs.', 2, 'Modificado Fecha, Administrador puede cancelar y Cancelar.'),
(84, '2007-11-19 18:11:00', 1, 12, '5', 'alvaro con danny a las 22:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(85, '2007-11-19 18:13:49', 1, 12, '5', 'alvaro con danny a las 22:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(86, '2007-11-19 18:15:33', 1, 12, '5', 'alvaro con danny a las 22:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(87, '2007-11-19 18:19:54', 1, 12, '5', 'alvaro con danny a las 22:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(88, '2007-11-19 18:20:41', 1, 12, '5', 'alvaro con danny a las 22:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(89, '2007-11-19 18:20:57', 1, 12, '5', 'alvaro con danny a las 22:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.'),
(90, '2007-11-19 18:37:49', 1, 12, '5', 'alvaro con danny a las 22:00 hs.', 2, 'Modificado Administrador puede cancelar y Cancelar.');

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'message', 'auth', 'message'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'permission', 'auth', 'permission'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'site', 'sites', 'site'),
(8, 'log entry', 'admin', 'logentry'),
(9, 'menu', 'menu', 'menu'),
(10, 'link', 'menu', 'link'),
(11, 'club', 'canchas', 'club'),
(12, 'reserva', 'canchas', 'reserva'),
(13, 'cancha', 'canchas', 'cancha'),
(22, 'club translation', 'canchas', 'clubtranslation'),
(15, 'registro', 'canchas', 'registro'),
(16, 'lista de espera', 'canchas', 'listadeespera'),
(17, 'cancha inhabilitada', 'canchas', 'canchainhabilitada'),
(18, 'sancion', 'canchas', 'sancion'),
(19, 'cuota', 'canchas', 'cuota'),
(20, 'socio', 'canchas', 'socio'),
(21, 'configuracion', 'canchas', 'configuracion'),
(23, 'sancion translation', 'canchas', 'sanciontranslation'),
(24, 'cuota translation', 'canchas', 'cuotatranslation'),
(25, 'cancha translation', 'canchas', 'canchatranslation'),
(28, 'flat page', 'flatpages', 'flatpage'),
(27, 'cancha inhabilitada translation', 'canchas', 'canchainhabilitadatranslation'),
(29, 'invitado', 'canchas', 'invitado');

--
-- Dumping data for table `django_flatpage`
--

INSERT INTO `django_flatpage` (`id`, `url`, `title`, `content`, `enable_comments`, `template_name`, `registration_required`) VALUES
(1, '/acerca/', 'Acerca de...', 'Acerca de django-bigua.\r\n\r\n * Repositorio: http://code.google.com/p/django-bigua/\r\n\r\n## Desarrolladores ##\r\n * Alvaro Mouriño\r\n * Daniel Alaniz', 0, '', 0);

--
-- Dumping data for table `django_flatpage_sites`
--

INSERT INTO `django_flatpage_sites` (`id`, `flatpage_id`, `site_id`) VALUES
(8, 1, 3),
(9, 1, 1);

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('87389e3bc2f4a94e1ddd40e6c466d56e', 'gAJ9cQEuOTMzZTRjMjkxYTM1OWQ0ZDk2YWY5YTcxZTJhYzEwMjQ=\n', '2007-10-23 22:51:47'),
('7b24979eecc1160dc63210e80e15fb32', 'gAJ9cQEuOTMzZTRjMjkxYTM1OWQ0ZDk2YWY5YTcxZTJhYzEwMjQ=\n', '2007-10-23 22:51:49'),
('c72959ff7eaf3c32d9470c0358e82719', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS4wNGNmOTRhMGE3NzE5MjBmYjYx\nMDU1YWFmYzIzZTc1Mw==\n', '2007-10-23 22:52:08'),
('0f3fbfd611dc7681695a9e01e0f0831e', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS4wNGNmOTRhMGE3NzE5MjBmYjYx\nMDU1YWFmYzIzZTc1Mw==\n', '2007-10-24 13:55:52'),
('e666dfb0d9f001ac8597a89351a1cdbc', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS4wNGNmOTRhMGE3NzE5MjBmYjYx\nMDU1YWFmYzIzZTc1Mw==\n', '2007-10-24 16:34:58'),
('b1e5fa9ec9f0d071f0ff979c36afda34', 'gAJ9cQEuOTMzZTRjMjkxYTM1OWQ0ZDk2YWY5YTcxZTJhYzEwMjQ=\n', '2007-11-09 00:17:44'),
('458fc7f4e21d0cdca3525590d1df22ba', 'gAJ9cQEuOTMzZTRjMjkxYTM1OWQ0ZDk2YWY5YTcxZTJhYzEwMjQ=\n', '2007-11-09 00:17:44'),
('e87408e57fb213eec1c352fed8efca4e', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS4wNGNmOTRhMGE3NzE5MjBmYjYx\nMDU1YWFmYzIzZTc1Mw==\n', '2007-12-03 05:41:40'),
('60d73e2e8ce20d724f1f37d84eb43f24', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS4wNGNmOTRhMGE3NzE5MjBmYjYx\nMDU1YWFmYzIzZTc1Mw==\n', '2007-11-18 22:12:58'),
('ade1367da7541d1ddfd664e790528493', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEDdS5mOWE1OGNmMWQwZmNiY2NlNjFk\nNjE4OWFhMDNiN2NkNg==\n', '2007-12-03 03:04:45'),
('1ff0bf05a7b2fc12ff274ad43c66a69a', 'gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigECdS40ZmUzZmQ0YTU2NGFiOWE0MjNk\nNTFiMjcwNjdmOTBjNQ==\n', '2007-12-03 03:08:11');

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'localhost:8000', 'tenis.bigua.com.uy'),
(2, 'sitio.com', ''),
(3, 'bigua.com.uy', 'bigua.com.uy');

--
-- Dumping data for table `menu_link`
--

INSERT INTO `menu_link` (`id`, `nombre`, `pagina_id`, `url`, `padre_id`, `posicion`, `desactivar`) VALUES
(1, 'Inicio', NULL, '/', NULL, 1, 0),
(2, 'Reservar', NULL, '/', NULL, 2, 0),
(3, 'Lista de Espera', NULL, '/listadeespera/', NULL, 3, 0),
(4, 'Notificaciones', NULL, '/notificaciones/', NULL, 4, 0),
(5, 'Acerca de...', 1, '', NULL, 5, 0),
(6, 'Zona Restringida', NULL, '/administrador/', NULL, 20, 0);

--
-- Dumping data for table `menu_menu`
--

INSERT INTO `menu_menu` (`id`, `nombre`, `descripcion`, `template`) VALUES
(1, 'Principal', 'El menú de navegación.', '');

--
-- Dumping data for table `menu_menu_links`
--

INSERT INTO `menu_menu_links` (`id`, `menu_id`, `link_id`) VALUES
(11, 1, 5),
(10, 1, 4),
(9, 1, 3),
(8, 1, 2),
(7, 1, 1),
(12, 1, 6);
